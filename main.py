from gogglesheet import GoogleSheet
from olxscraper import OlxScraper
from data_manager import DataManager
import os
from dotenv import load_dotenv

from telegram import Telegram

if __name__ == "__main__":
    load_dotenv()
    SHEET_ID = os.getenv("SHEET_ID")
    SHEET_NAME = "Arkusz1"
    OLX_URL = "https://www.olx.pl/motoryzacja/samochody/?search%5Bfilter_float_price:from%5D=8000&search%5Bfilter_float_price:to%5D=12500"

    sheet = GoogleSheet(SHEET_ID, SHEET_NAME)
    scraper = OlxScraper(OLX_URL)
    manager = DataManager(sheet)
    telegram = Telegram()

    new_data = manager.update_sheet_with_unique(scraper)
    telegram_string = manager.format_data_as_message(new_data)
    telegram.send_message(telegram_string)