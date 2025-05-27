import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()
        return content
    else:
        print(f"Error: {response.status_code}")
        return None

url = "https://www.example.com"
content = fetch_content(url)
if content is not None:
    print(content)
