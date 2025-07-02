from gogglesheet import GoogleSheet
from olxscraper import OlxScraper

class DataManager:
    def __init__(self, sheet: GoogleSheet):
        self.sheet = sheet

    def get_unique_from_olx(self, olx: OlxScraper) -> list[dict]:
        # Pobierz wszystkie już zapisane linki z arkusza
        seen_links = {row.get("Link") for row in self.sheet.read_all() if "Link" in row}
        unique_from_olx = []

        for d in olx.fetch_listings():
            link = d.get("Link")
            if link and link not in seen_links:
                unique_from_olx.append(d)
        return unique_from_olx

    def update_sheet_with_unique(self, olx: OlxScraper):
        new_data = self.get_unique_from_olx(olx)
        self.sheet.add_rows(new_data)
        return new_data

    def format_data_as_message(self, data: list[dict]) -> str:
        message = ""
        for i, row in enumerate(data, 1):
            message += f"{i}. {row.get('Title', '')}\n"
            message += f"   Cena: {row.get('Price', '')}\n"
            message += f"   Rok: {row.get('Year', '')}, Przebieg: {row.get('Milage', '')}\n"
            message += f"   Link: {row.get('Link', '')}\n\n"
        return message.strip()