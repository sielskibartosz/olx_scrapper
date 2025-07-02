from gogglesheet import GoogleSheet
from olxscraper import OlxScraper

class DataManager:
    def __init__(self, sheet: GoogleSheet):
        self.sheet = sheet

    def get_unique_from_olx(self, olx: OlxScraper) -> list[dict]:
        seen = set(tuple(sorted(d.items())) for d in self.sheet.read_all())
        unique_from_olx = []

        for d in olx.fetch_listings():
            items = tuple(sorted(d.items()))
            if items not in seen:
                unique_from_olx.append(d)
        return unique_from_olx

    def update_sheet_with_unique(self, olx: OlxScraper):
        new_data = self.get_unique_from_olx(olx)
        self.sheet.add_rows(new_data)
        return len(new_data)
