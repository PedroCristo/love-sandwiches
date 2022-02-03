import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('./controllers/creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Love_sandwiches')



def get_sales_data():

    """
    Get sales figures from the user
    """

    print("Please enter sales data from the last maeket.")
    print("Data should be six numbers, sparate by commas")
    print("Example: 10, 20, 25, 51\n")

    data_str = input("Enter your data here: ")
    print(f"The data provied by you is {data_str}")


get_sales_data()