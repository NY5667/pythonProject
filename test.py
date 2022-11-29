# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import pyodbc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = '10.54.4.21'
    database = 'ADP'
    username = 'sa'
    password = 'Supcon@1304'
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password+';ENCRYPT=yes;TrustServerCertificate=yes;')
    cursor = cnxn.cursor()

    #Sample select query
    cursor.execute("SELECT * FROM SESGIS_CUSTOM_THEMATICS WHERE VALID = 1")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
