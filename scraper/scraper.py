import requests
from bs4 import BeautifulSoup
import json

def fetch_business_url(business_name):
    url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": ""}
    params = {"q": business_name, "count": 1, "responseFilter": "Webpages"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    search_results = response.json()
    try:
        business_url = search_results["webPages"]["value"][0]["url"]
    except (KeyError, IndexError):
        business_url = "URL not found"

    return business_url

def fetch_and_parse(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_alt_texts(soup):
    divs = soup.find_all('div', class_='merch-full')

    alt_texts = []

    for div in divs:
        img = div.find('img')
        if img and 'alt' in img.attrs:
            alt_texts.append(img['alt'])

    return alt_texts

def main():
    page = 1
    previous_alts = None
    results = {}

    while True:
        url = f"https://www.airnewzealand.co.nz/airpoints-mall/az?orderBy=name&letter=&page={page}"
        print(f"Scraping page: {page}")

        soup = fetch_and_parse(url)
        current_alts = extract_alt_texts(soup)

        if current_alts == previous_alts:
            print("Detected repeated data, stopping...")
            break

        previous_alts = current_alts

        for alt in current_alts:
            url = fetch_business_url(alt)
            results[alt] = {"name": alt, "url": url}
            print(json.dumps(results, indent=4))

        page += 1

    with open('business_urls.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    main()
