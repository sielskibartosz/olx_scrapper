import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.pl/d/motoryzacja/samochody/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź wszystkie ogłoszenia
divs = soup.select('div[data-cy="l-card"]')

# Przejdź przez każde ogłoszenie
for i, div in enumerate(divs, 1):
    # Szukamy linku
    link_tag = div.select_one('a[href]')
    link = "https://www.olx.pl" + link_tag['href'] if link_tag else "Brak linku"

    # Szukamy ceny
    price_tag = div.select_one('p[data-testid="ad-price"]')
    price = price_tag.get_text(strip=True) if price_tag else "Brak ceny"

    # Wypisz
    print(f"{i}. Link: {link}")
    print(f"   Cena: {price}")
