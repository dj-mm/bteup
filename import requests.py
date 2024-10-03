import requests
import hashlib
import time
from datetime import datetime
from bs4 import BeautifulSoup

def get_website_hash(url):
    try:
        # Disable SSL verification (not recommended for production)
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        return hashlib.sha256(soup.body.get_text(strip=True).encode('utf-8')).hexdigest()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
import requests
import hashlib
import time
from datetime import datetime
from bs4 import BeautifulSoup

def get_website_hash(url):
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        return hashlib.sha256(soup.body.get_text(strip=True).encode('utf-8')).hexdigest()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

url = "http://result.bteevaluation.co.in/even/main/"
previous_hash = get_website_hash(url)
check_interval = 30  # Check every 30 seconds

while True:
    current_hash = get_website_hash(url)
    if current_hash is None:
        continue  # Skip if there's an error fetching the URL
    if previous_hash != current_hash:
        print(f"Update on {url} at {datetime.now().strftime('%H:%M:%S')}")
        previous_hash = current_hash
    time.sleep(check_interval)
