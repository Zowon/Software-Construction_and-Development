import os
import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = "https://au.edu.pk/pages/Faculties/Engineering/Departments/Electrical/Elec_Faculty.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory for storing faculty images
if not os.path.exists('faculty_images'):
    os.makedirs('faculty_images')

# Open CSV file to write faculty data
with open('faculty_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Designation', 'Image URL', 'Profile URL'])  # Header row

    # Select all faculty blocks
    faculty_blocks = soup.select('#ContentPlaceHolder_header_footer_ContentPlaceHolder_Content_divFaculty .col-md-3')

    # Base URL for constructing full links
    base_url = "https://au.edu.pk"

    for block in faculty_blocks:
        # Extract name
        name = block.select_one('.text-center b').get_text(strip=True)

        # Extract designation (typically the second <b> tag in the same p element)
        designation = block.select('.text-center b')[1].get_text(strip=True)

        # Extract image URL
        image_url = base_url + block.find('img')['src'][5:]  # Adjusting relative path

        # Extract profile URL
        profile_url = base_url + block.find('a')['href'][5:]  # Adjusting relative path

        # Download and save the image
        image_filename = os.path.join('faculty_images', f"{name.replace(' ', '_')}.jpg")
        img_response = requests.get(image_url)
        with open(image_filename, 'wb') as img_file:
            img_file.write(img_response.content)

        # Write faculty data to CSV
        writer.writerow([name, designation, image_url, profile_url])

# Create a text file with university information
with open('university_info.txt', 'w') as uni_file:
    uni_file.write("University Name: Air University\n")
    uni_file.write(f"Faculty Webpage URL: {url}\n")

print("Faculty data saved to faculty_data.csv and images downloaded in faculty_images folder")
print("University information saved to university_info.txt")
