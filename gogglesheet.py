import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet:
    def __init__(self, sheet_id: str, sheet_name: str):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open_by_key(sheet_id).worksheet(sheet_name)

    def read_all(self) -> list[dict]:
        return self.sheet.get_all_records()

    def add_rows(self, rows: list[dict]):
        if not rows:
            return
        headers = self.sheet.row_values(1)
        values = [[row.get(header, "") for header in headers] for row in rows]
        # self.sheet.append_rows(values)
        for row in reversed(values):
            self.sheet.insert_row(row, index=2)