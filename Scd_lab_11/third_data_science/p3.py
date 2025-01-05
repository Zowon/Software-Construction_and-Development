import os
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import csv
import threading

# URLs to be processed
target_urls = [
    "https://towardsdatascience.com/concurrency-in-python-fe8b39edfba5"
]

# Output file paths
output_csv = "scraped_articles.csv"
output_pdf_directory = "pdf_articles"

# Utility to handle text encoding for FPDF compatibility
def clean_text_for_pdf(input_text):
    return input_text.encode('latin-1', 'replace').decode('latin-1')

# Function to identify and retrieve main article content
def fetch_article_text(soup_object):
    article_text = ""
    article_container = soup_object.find('article') or soup_object.find('div', class_='content')
    if article_container:
        for paragraph in article_container.find_all('p'):
            article_text += paragraph.get_text(strip=True) + "\n\n"
    else:
        for paragraph in soup_object.find_all('p'):
            article_text += paragraph.get_text(strip=True) + "\n\n"
    return article_text.strip()

# Individual webpage scraper
def process_single_page(web_url, scraped_data):
    try:
        response = requests.get(web_url)
        response.raise_for_status()
        page_content = BeautifulSoup(response.text, 'html.parser')

        # Fetch the title
        title_element = page_content.find('h1')
        title = title_element.get_text(strip=True) if title_element else "Title Unavailable"

        # Fetch the date of publication
        date_element = page_content.find('time')
        publication_date = date_element.get('datetime') if date_element and date_element.has_attr('datetime') else "Date Unknown"

        # Placeholder for difficulty level
        difficulty = "N/A"

        # Extract brief summary (assumes first <p> contains the introduction)
        summary_element = page_content.find('p')
        summary = summary_element.get_text(strip=True)[:300] if summary_element else "Summary Not Found"

        # Extract and save content as a PDF
        article_text = fetch_article_text(page_content)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, clean_text_for_pdf(article_text))
        sanitized_title = clean_text_for_pdf(title[:50].replace(' ', '_'))
        pdf.output(f"{output_pdf_directory}/{sanitized_title}.pdf")

        # Store metadata for CSV export
        scraped_data.append({
            "Source": web_url.split('/')[2],
            "Article Title": title,
            "Page URL": web_url,
            "Date Published": publication_date,
            "Difficulty": difficulty,
            "Summary": summary
        })

    except Exception as error:
        print(f"Error processing {web_url}: {error}")

# Threading for concurrent scraping
def scrape_websites(url_list):
    threads = []
    collected_data = []
    for url in url_list:
        thread = threading.Thread(target=process_single_page, args=(url, collected_data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return collected_data

# Function to export data to CSV
def write_data_to_csv(data):
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Source", "Article Title", "Page URL", "Date Published", "Difficulty", "Summary"])
        writer.writeheader()
        writer.writerows(data)

# Main driver function
def execute_scraping():
    print("Initiating scraping tasks...")
    scraped_results = scrape_websites(target_urls)
    write_data_to_csv(scraped_results)
    print(f"Scraping completed. Data saved in {output_csv}. PDFs are stored in {output_pdf_directory}")

if __name__ == "__main__":
    if not os.path.exists(output_pdf_directory):
        os.makedirs(output_pdf_directory)
    execute_scraping()
