import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Define the scope and authorize the client
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")

# Convert the JSON string to a dictionary
creds = json.loads(credentials_json)
creds = Credentials.from_service_account_info(creds, scopes=scopes)
client = gspread.authorize(creds)

# Open the Google Sheet by ID
sheet_id = "1Wr_inx5FeX-QrOr9iC4C8AnlcQXYwHEZ_IamoGEqp9Q"
workbook = client.open_by_key(sheet_id)
sheet = workbook.sheet1

def update_feedback(name, feedback):
    """
    Appends a name and feedback to the Google Sheet.

    Args:
        name (str): The name to be added.
        feedback (str): The feedback to be added.
    """
    # Get the next available row number
    next_row = len(sheet.get_all_values()) + 1

    # Append the name and feedback to the sheet
    sheet.update_cell(next_row, 1, name)
    sheet.update_cell(next_row, 2, feedback)

# Example usage
#update_feedback("John Doe", "This is a sample feedback")