from logging import exception

import  gspread
from oauth2client.service_account import ServiceAccountCredentials

def fetch_data(sheet_name):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheets.readonly'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

    client = gspread.authorize(credentials)


    try:
        sheet = client.open(sheet_name).sheet1

        data = sheet.get_all_records()
        return  data


    except Exception as e:
        raise ValueError(f"Sheet {sheet_name} does not exist")
    

