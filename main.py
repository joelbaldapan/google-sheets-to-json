# https://docs.google.com/spreadsheets/d/1q1vu3KSARMWUudyybNdjNe0oTeQzh_MeI63r7-pupg0/edit?gid=0#gid=0
import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

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
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    # Main parser
    workbook = client.open_by_key(sheet_id)

if __name__ == "__main__":
    client = initialize_client()
    run_json_parser(client)
