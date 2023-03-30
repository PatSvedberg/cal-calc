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
    print(f"Welcome '{username}' what did you do today?\n")
    print("Use the keys 1-2 to select activity:\n")
    print("1 - Jogging")
    print("2 - Swimming\n")
    
    activity = input("Select activity (1-2): ")
    if activity == '1':
        jogging()
    elif activity == '2':
        swimming()
    else:
        print("Invalid input, please select 1 or 2.")

def jogging():
    '''
    Function for jogging activity
    '''
    jogging = input("How many kilometers did you jog?: ")
    
def swimming():
    '''
    Function for swimming activity
    '''
    swimming = input("How many kilometers did you swim?: ")

if __name__ == '__main__':
    create_new_worksheet()