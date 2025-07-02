import datetime
import re

import requests
from bs4 import BeautifulSoup

class OlxScraper:
    def __init__(self, url: str):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def fetch_listings(self) -> list[dict]:
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        divs = soup.select('div[data-cy="l-card"]')

        listings = []
        # dt = datetime.now()
        # dt = dt.replace(second=0, microsecond=0)
        for div in divs:
            # Tytuł
            title_tag = div.select_one('h4.css-1g61gc2')
            title = title_tag.get_text(strip=True) if title_tag else "Brak tytułu"

            # Link
            link_tag = div.select_one('a[href]')
            link = "https://www.olx.pl" + link_tag['href'] if link_tag else "Brak linku"

            # Cena
            price_tag = div.select_one('p[data-testid="ad-price"]')
            price = price_tag.get_text(strip=True) if price_tag else "Brak ceny"
            match = re.findall(r'\d+', price)
            price = int(''.join(match)) if match else None

            # Rok i przebieg
            details = div.select_one('span.css-6as4g5')
            if details:
                year_milage = details.get_text(strip=True)
                parts = year_milage.split("-")
                year = int(parts[0].strip()) if len(parts) > 0 else "Brak"
                milage = int(parts[1].strip()[:-3].replace(" ", "")) if len(parts) > 1 else "Brak"
            else:
                year = "Brak"
                milage = "Brak"

            listings.append({
                "Title": title,
                "Link": link,
                "Price": price,
                "Year": year,
                "Milage": milage
            })

        # # Time
        # dt = datetime.now()
        # listings.append()

        return listings
