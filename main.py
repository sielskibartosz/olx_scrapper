from gogglesheet import GoogleSheet
from olxscraper import OlxScraper
from data_manager import DataManager
import os
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    SHEET_ID = os.getenv("SHEET_ID")
    SHEET_NAME = "Arkusz1"
    OLX_URL = "https://www.olx.pl/d/motoryzacja/samochody/"

    sheet = GoogleSheet(SHEET_ID, SHEET_NAME)
    scraper = OlxScraper(OLX_URL)
    manager = DataManager(sheet)

    new_count = manager.update_sheet_with_unique(scraper)
    print(f"Dodano {new_count} nowych rekordów.")
