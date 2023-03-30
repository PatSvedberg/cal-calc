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


def insert_weight():
    '''
    Creates a value of the weight to calculate calories burnt
    '''
    # Ask the user to enter their weight and convert it to an integer
    while True:
        weight = input("Enter your current weight: ")
        try:
            weight = int(weight)
            break
        except ValueError:
            # If the user enters an invalid input, print an error message
            print("Error: Weight must be an integer.")

    return weight


def create_new_worksheet():
    '''
    Creates a new worksheet with the same name as the user
    '''
    username = create_user()
    weight = insert_weight()
    worksheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
    worksheet.update_cell(1, 1, "Weight(kg)")
    worksheet.update_cell(2, 1, weight)
    worksheet.update_cell(1, 2, "Jogging Distance(km)")
    worksheet.update_cell(1, 3, "Swimming Distance(km)")

    print(f"Welcome '{username}' what did you do today?\n")  
    print("1 - Jogging")
    print("2 - Swimming\n")  
    activity = input("Select activity (1-2): ")

    if activity == '1':
        jogging(worksheet)  # Pass the worksheet object to the jogging function
    elif activity == '2':
        swimming(worksheet)  # Pass the worksheet object to the swimming function
    else:
        print("Invalid input, please select 1 or 2.")


def jogging(worksheet):
    '''
    Function for jogging activity
    '''
    jogging_time = input("How many minutes did you jog?: ")
    column_values = worksheet.col_values(2)  # Get all the values in the second column of the worksheet
    next_row = len(column_values) + 1  # Find the next empty row in the second column
    worksheet.update_cell(next_row, 2, jogging_time)  # Add jogging time to the next empty slot in the second column
    calculate_jog_value(worksheet)


def swimming(worksheet):
    '''
    Function for swimming activity
    '''
    swimming_distance = input("How many kilometers did you swim?: ")
    column_values = worksheet.col_values(3)  # Get all the values in the third column of the worksheet
    next_row = len(column_values) + 1  # Find the next empty row in the third column
    worksheet.update_cell(next_row, 3, swimming_distance)  # Add swimming distance to the next empty slot in the third column


def calculate_jog_value(worksheet):
    '''
    Print last value of jogging
    '''
    jog_values = worksheet.col_values(2)
    last_value = int(jog_values[-1]) 
    test_calc = last_value * 3

    print(f"Last value in this columns is {last_value}")
    print(f"Check calclation for fun... {test_calc}")


def main():
    '''
    Main function
    '''
    create_new_worksheet()

main()
