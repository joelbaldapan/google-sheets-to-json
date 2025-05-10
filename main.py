# https://docs.google.com/spreadsheets/d/1q1vu3KSARMWUudyybNdjNe0oTeQzh_MeI63r7-pupg0/edit?gid=0#gid=0
import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
import json

DEFAULT_OUTPUT_FILE_PATH = "output/"
DEFAULT_OUTPUT_FILE_NAME = "output.json"
DEFAULT_INDENTS = 2

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
    # Use environment variables for Sheet ID and file path
    load_dotenv()
    workbook_id = os.getenv("GOOGLE_SHEET_ID")
    worksheet_id = os.getenv("WORKSHEET_NAME")
    path = os.getenv("OUTPUT_FILE_PATH", DEFAULT_OUTPUT_FILE_PATH)
    filename = os.getenv("OUTPUT_FILE_NAME", DEFAULT_OUTPUT_FILE_NAME)
    indents = os.getenv("INDENTS", DEFAULT_INDENTS)

    # Defaults
    if not path:
        path = DEFAULT_OUTPUT_FILE_PATH
    if not filename:
        filename = DEFAULT_OUTPUT_FILE_NAME
    if not indents:
        indents = DEFAULT_INDENTS

    # Main parser
    wb = client.open_by_key(workbook_id)
    sht = wb.worksheet(worksheet_id)
    list_of_dicts = sht.get_all_records()

    # Create JSON file
    os.makedirs(path, exist_ok=True)
    file_path = f"{path}{filename}"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(list_of_dicts, f, indent=indents)

    print("Success!")
    print(f"Exported JSON file to: {path}{filename}")

if __name__ == "__main__":
    client = initialize_client()
    run_json_parser(client)
