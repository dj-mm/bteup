import requests
import hashlib
import time
from datetime import datetime
from bs4 import BeautifulSoup

def get_website_hash(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        main_content = soup.body.get_text(strip=True)
        return hashlib.sha256(main_content.encode('utf-8')).hexdigest()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

url = "http://result.bteevaluation.co.in/even/main/"
previous_hash = get_website_hash(url)
check_interval = 10

try:
    while True:
        current_hash = get_website_hash(url)
        if current_hash and previous_hash != current_hash:
            update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Detected update at: {update_time}")
            previous_hash = current_hash
        else:
            print("No update detected.")
        time.sleep(check_interval)
except KeyboardInterrupt:
    print("Stopped by user.")
