# https://docs.google.com/spreadsheets/d/1q1vu3KSARMWUudyybNdjNe0oTeQzh_MeI63r7-pupg0/edit?gid=0#gid=0
import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
import json

OUTPUT_FILE_PATH = "output/"
OUTPUT_FILE_NAME = "output.json"

def initialize_client():
    """Initializes client. Returns clien object"""
    # Use environment variables for credentials
    load_dotenv()
    credentials_path = os.getenv("GOOGLE_SHEET_CREDENTIALS")

    # Authorize
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
    client = gspread.authorize(creds)
    return client

# Main
def run_json_parser(client):
    """Runs JSON parser. Arg: client object"""
    # Use environment variables for Sheet ID
    load_dotenv()
    workbook_id = os.getenv("GOOGLE_SHEET_ID")
    worksheet_id = os.getenv("WORKSHEET_NAME")

    # Main parser
    wb = client.open_by_key(workbook_id)
    sht = wb.worksheet(worksheet_id)
    list_of_dicts = sht.get_all_records()

    # Create json file
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True)
    file_path = f"{OUTPUT_FILE_PATH}/{OUTPUT_FILE_NAME}"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(list_of_dicts, f, indent=4)

    print("DONE")

if __name__ == "__main__":
    client = initialize_client()
    run_json_parser(client)
