import requests
from bs4 import BeautifulSoup
import random

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.get_text()
            return content
        else:
            raise Exception(f"Failed to retrieve the page at {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_and_parse_random(url):
    random_url = f"https://example.com{random.randint(0, 100)}"
    try:
        content = fetch_and_parse(random_url)
        return content
    except Exception as e:
        print(f"An error occurred while fetching the page at {random_url}: {e}")

def main():
    urls = ["https://example.com/1", "https://example.com/2"]
    
    for url in urls:
        try:
            content = fetch_and_parse_random(url)
            print(content)
        except Exception as e:
            print(f"An error occurred while fetching the page at {url}: {e}")

if __name__ == "__main__":
    main()
