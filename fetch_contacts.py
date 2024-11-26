import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

def fetch_contacts():
    """Fetch contacts from Google Sheets."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(credentials)

    try:
        logging.info("Accessing Google Sheet...")
        spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID")  # Replace with your Sheet URL
        sheet = spreadsheet.sheet1
        data = sheet.get_all_records()
        contacts = [{"name": row["Name/Handle"], "email": row["Email Address"]} for row in data if row.get("Email Address")]
        return contacts
    except Exception as e:
        logging.error(f"Failed to fetch contacts: {e}")
        raise
