import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_sheets(data):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Leads").sheet1

    for lead in data:
        sheet.append_row([
            lead.get("username"),
            lead.get("bio"),
            lead.get("followers"),
            lead.get("engagement"),
            lead.get("dm")
        ])
