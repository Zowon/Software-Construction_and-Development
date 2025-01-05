import requests
from bs4 import BeautifulSoup
import csv
from fpdf import FPDF
import os

# Main URL to scrape
source_url = "https://realpython.com/python-concurrency/"

# Paths for outputs
csv_output = "python_articles_overview.csv"
pdf_directory = "exported_pdfs"

# Function to handle special Unicode replacements
def clean_unicode(text):
    """Convert problematic Unicode symbols to plain equivalents."""
    unicode_map = {
        '\u2019': "'",  # Right single quote
        '\u2018': "'",  # Left single quote
        '\u201c': '"',  # Left double quote
        '\u201d': '"',  # Right double quote
        '\u2014': "-",  # Em dash
        '\u2013': "-",  # En dash
        '\u2026': "...",  # Ellipsis
    }
    for old_char, new_char in unicode_map.items():
        text = text.replace(old_char, new_char)
    return text

# Function to find linked articles
def fetch_related_links(source):
    """Extract related Python concurrency articles."""
    try:
        response = requests.get(source, timeout=10)
        response.raise_for_status()

        page = BeautifulSoup(response.content, "html.parser")

        # Extract title of the primary article
        main_heading = page.find("h1").get_text(strip=True) if page.find("h1") else "Title Not Found"
        print(f"Main article title: {main_heading}")

        # Locate the section with related links
        related_section = page.find("section", {"class": "related-articles"})
        if not related_section:
            print("No section for related articles was detected.")
            return []

        # Gather up to 3 related article links
        related_links = []
        for anchor in related_section.find_all("a", href=True):
            href = anchor["href"]
            if "python-concurrency" in href and href not in related_links:
                related_links.append(href)

        # Append base URL to relative paths and return top 3
        return [f"https://realpython.com{link}" for link in related_links[:3]]

    except Exception as error:
        print(f"Error while fetching related links: {error}")
        return []

# Function to scrape article content
def scrape_article_content(link):
    """Retrieve the article's title and text content."""
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()

        parsed_page = BeautifulSoup(response.content, "html.parser")
        article_title = parsed_page.find("h1").get_text(strip=True) if parsed_page.find("h1") else "Untitled"
        body_content = parsed_page.find("div", {"class": "article-body"})
        body_text = body_content.get_text(strip=True) if body_content else "No Content Available"

        return article_title, clean_unicode(body_text)

    except Exception as error:
        print(f"Failed to scrape content from {link}: {error}")
        return None, None

# Function to create a PDF for an article
def create_pdf(article_title, article_body, file_name):
    """Generate a PDF document for an article."""
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Article: " + article_title, ln=True, align='C')

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"\n{article_body}")

        # Ensure output directory exists
        os.makedirs(pdf_directory, exist_ok=True)
        pdf.output(f"{pdf_directory}/{file_name}.pdf")

        print(f"PDF generated for: {article_title}")

    except Exception as error:
        print(f"Error creating PDF for {article_title}: {error}")

# Function to write data to a CSV
def export_to_csv(rows):
    """Save the collected data to a CSV file."""
    try:
        with open(csv_output, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Website", "Title", "URL", "Date Published", "Difficulty", "Snippet"])
            writer.writerows(rows)
        print(f"Data written to {csv_output} successfully.")

    except Exception as error:
        print(f"Error saving to CSV: {error}")

# Main logic for scraping and exporting
if __name__ == "__main__":
    # Fetch related articles
    related_links = fetch_related_links(source_url)

    # Initialize data for export
    collected_data = []
    primary_data_row = ["Real Python", "Concurrency Overview", source_url, "N/A", "N/A", "Key Article Summary"]
    collected_data.append(primary_data_row)

    # Scrape and generate PDF for the primary article
    main_title, main_text = scrape_article_content(source_url)
    if main_title and main_text:
        create_pdf(main_title, main_text, "Primary_Concurrency_Article")
        collected_data[0][5] = main_text[:300]  # Add snippet to CSV row

    # Scrape and generate PDFs for related articles
    for index, article_link in enumerate(related_links, start=1):
        article_title, article_body = scrape_article_content(article_link)
        if article_title and article_body:
            create_pdf(article_title, article_body, f"Related_Article_{index}")
            collected_data.append(["Real Python", article_title, article_link, "N/A", "N/A", article_body[:300]])

    # Save all data to CSV
    export_to_csv(collected_data)
