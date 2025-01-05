import requests
from bs4 import BeautifulSoup
import csv
import pdfkit
from concurrent.futures import ThreadPoolExecutor

# Links to scrape content from
urls_to_scrape = [
    "https://www.geeksforgeeks.org/python-program-with-concurrency/?ref=gcse_outind",
    "https://realpython.com/python-concurrency/",
    "https://towardsdatascience.com/concurrency-in-python-4c1649ca01c1"
]

# Function to extract article content
def extract_content(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        page_content = BeautifulSoup(response.text, "html.parser")

        # Extracting article details
        article_title = page_content.find('h1').text.strip() if page_content.find('h1') else "Title Not Found"
        article_date = page_content.find('time', {'datetime': True})
        article_date = article_date['datetime'] if article_date else "Date Unknown"
        complexity_level = "Level Unavailable"  # Update if the website provides such info
        summary_element = page_content.find('p')
        content_summary = summary_element.text.strip()[:300] if summary_element else "Summary Not Available"

        return {
            "Source": link.split("//")[1].split("/")[0],
            "Headline": article_title,
            "Link": link,
            "Date Published": article_date,
            "Difficulty": complexity_level,
            "Description": content_summary
        }
    except Exception as error:
        print(f"Error processing {link}: {error}")
        return None

# Function to generate a PDF from a URL
def generate_pdf(link, output_file):
    try:
        pdfkit.from_url(link, output_file)
        print(f"PDF Created: {output_file}")
    except Exception as error:
        print(f"Failed to create PDF for {link}: {error}")

# Function to save data into a CSV file
def write_to_csv(data, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=["Source", "Headline", "Link", "Date Published", "Difficulty", "Description"])
        csv_writer.writeheader()
        csv_writer.writerows(data)

# Main logic for scraping and saving data
def run_scraper():
    gathered_data = []
    pdf_outputs = []

    # Use threads to accelerate the process
    with ThreadPoolExecutor(max_workers=5) as executor:
        extraction_results = list(executor.map(extract_content, urls_to_scrape))
        gathered_data = [item for item in extraction_results if item]  # Exclude None entries

    # Save extracted information to CSV
    csv_output = "content_overview.csv"
    write_to_csv(gathered_data, csv_output)
    print(f"CSV File Saved: {csv_output}")

    # Generate PDFs for top results
    for idx, record in enumerate(gathered_data):
        pdf_output = f"highlighted_article_{idx+1}.pdf"
        generate_pdf(record["Link"], pdf_output)
        pdf_outputs.append(pdf_output)

    print(f"PDFs Generated: {pdf_outputs}")

if __name__ == "__main__":
    run_scraper()
