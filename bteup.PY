import requests
import hashlib
import time
from datetime import datetime
from bs4 import BeautifulSoup

# Function to get the hash of specific content in the webpage
def get_website_hash(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract specific content (adjust this to fit the relevant part of the website)
        # For example, if we want to check the body content only:
        main_content = soup.body.get_text(strip=True)  # Extract text content from the body
        
        return hashlib.sha256(main_content.encode('utf-8')).hexdigest()
    except requests.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

# URL of the website
url = "https://bteup.ac.in/webapp/home.aspx"

# Get the initial hash of the webpage
previous_hash = get_website_hash(url)

# Interval (in seconds) between checks
check_interval = 10  # Adjust this to however frequently you want to check

while True:
    current_hash = get_website_hash(url)

    # Check if the hash has changed
    if current_hash and previous_hash != current_hash:
        update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Detected update at: {update_time}")
        previous_hash = current_hash
    else:
        print("No update detected.")

    # Wait for the next check
    time.sleep(check_interval)
