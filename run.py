import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calCalc')

def create_user():
    '''
    Creates a new user with the name given
    '''
    username = input("Enter username: ")
    return username

def create_new_worksheet():
    '''
    Creates a new worksheet with the same name as the user
    '''
    username = create_user()
    worksheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
    print(f"New worksheet '{username}' created successfully!")

if __name__ == '__main__':
    create_new_worksheet()