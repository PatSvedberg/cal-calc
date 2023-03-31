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

JOG_MET = 7
SWIM_MET = 10


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
    worksheet.update_cell(2, 1, int(weight))
    worksheet.update_cell(1, 2, "Jogging Time. Minutes")
    worksheet.update_cell(1, 3, "Jog MET value:")
    worksheet.update_cell(2, 3, JOG_MET)
    worksheet.update_cell(1, 4, "Swimming Time. Minutes")
    worksheet.update_cell(1, 5, "Swim MET value:")
    worksheet.update_cell(2, 5, SWIM_MET)

    print(f"Welcome '{username}' what did you do today?\n")  
    print("1 - Jogging")
    print("2 - Swimming\n")  
    activity = input("Select activity (1-2): ")

    if activity == '1':
        jogging(worksheet, weight)  # Pass the worksheet object to jog function
        calculate_jog_value(worksheet, weight)
    elif activity == '2':
        swimming(worksheet, weight)  # Pass the worksheet object to swim function
    else:
        print("Invalid input, please select 1 or 2.")


def jogging(worksheet, weight):
    '''
    Function for jogging activity
    '''
    jogging_time = input("How many minutes did you jog?: ")
    column_values = worksheet.col_values(2)  # Get all values in 2nd column of worksheet
    next_row = len(column_values) + 1  # Find next empty row in the 2nd column
    worksheet.update_cell(next_row, 2, jogging_time)  # Add jogging time to the next empty slot in the second column
    calculate_jog_value(worksheet, weight)


def swimming(worksheet, weight):
    '''
    Function for swimming activity
    '''
    swimming_distance = input("How many minutes did you swim?: ")
    column_values = worksheet.col_values(4)  # Get all the values in the third column of the worksheet
    next_row = len(column_values) + 1  # Find next empty row in the 4th column
    worksheet.update_cell(next_row, 4, swimming_distance)  # Add swimming distance to the next empty slot in the third column
    calculate_swim_value(worksheet, weight)


def calculate_jog_value(worksheet, weight):
    '''
    Print last value of jogging
    '''
    jog_min = worksheet.col_values(2)
    jog_time = int(jog_min[-1])

    calories_burned = round((JOG_MET * 3.5 * weight * jog_time) / 200)
    print("Calories burned:", calories_burned)


def calculate_swim_value(worksheet, weight):
    '''
    Print last value of swimming
    '''
    swim_min = worksheet.col_values(4)
    swim_time = int(swim_min[-1])

    calories_burned = round((SWIM_MET * 3.5 * weight * swim_time) / 200)
    print("Calories burned:", calories_burned)


def main():
    '''
    Main function
    '''
    create_new_worksheet()


main()
