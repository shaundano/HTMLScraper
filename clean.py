import os
from bs4 import BeautifulSoup

# Directory paths
raw_data_folder = "Uncleaned data"
cleaned_data_folder = "Cleaned data"

# Ensure the cleaned data folder exists
if not os.path.exists(cleaned_data_folder):
    os.makedirs(cleaned_data_folder)

# List all HTML files in the raw data folder
html_files = [f for f in os.listdir(raw_data_folder) if f.endswith(".txt")]

# Process each HTML file
for html_file in html_files:
    # Read HTML data from the raw data file
    with open(os.path.join(raw_data_folder, html_file), "r", encoding="utf-8") as file:
        html_data = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_data, 'html.parser')

    # Define the classes to keep (same as before)
    relevant_classes = [
        "update-components-actor__name",
        "update-components-actor__meta-link",
        "social-details-social-counts__reactions-count",
        "social-details-social-counts__comments",
        "social-details-social-counts__reactions",
        "social-details-social-counts__item",
        "update-components-actor__description",
        "update-components-actor__sub-description-link",
        "update-components-update-v2__description",
        "update-components-article__title",
        "update-components-article__subtitle",
    ]

    # Find all <li> tags with the specified class
    post_containers = soup.find_all("li", class_="profile-creator-shared-feed-update__container")

    # Create a cleaned data file name
    cleaned_file_name = os.path.splitext(html_file)[0] + "_clean.txt"
    
    # Construct the path to the cleaned data file
    cleaned_file_path = os.path.join(cleaned_data_folder, cleaned_file_name)

    # Create a text file and write the relevant data with comments
    with open(cleaned_file_path, "w", encoding="utf-8") as output_file:
        for container in post_containers:
            # Add a comment marker before the <li> tag
            output_file.write("<!-- NEW POST -->\n")
            # Write the <li> tag
            output_file.write(str(container) + "\n")

    print(f"Cleaned data saved to: {cleaned_file_path}")
