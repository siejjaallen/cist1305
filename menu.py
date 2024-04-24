import sqlite3

#Create a connection to the database
conn = sqlite3.connect('example.db')

# Create a cursor
data = conn.cursor()

#Create a table
data.execute('''CREATE TABLE IF NOT EXISTS stocks
             (data text,symbol text, qty real, price real)''')

#display menu

print("1. Buy a stock")
print("2. Sell a stock")
print("3. Exit program")

menu_selection = int(input("Enter your selection: "))

def buy():
    if menu_selection == 1:
        date = input ("Enter the date: ")
        stock = input ("Enter the stock symbol: ")
        number = input ("How many stocks: ")
        money = input ("Price of the stock: ")
        data.execute(f'INSERT INTO stocks VALUES ({date}, "{stock}", {number}, {money})')
buy()

def sell():
    if menu_selection == 2:
        date = input ("Enter the date: ")
        stock = input ("Enter the stock symbol: ")
        number = input ("How many stocks: ")
        money = input ("Price of the stock: ")
        data.execute(f'INSERT INTO stocks VALUES ({date},"{stock}", {number}, {money})')
sell() 

def exit():
    if menu_selection == 3:
        print("You are exiting the program, here are your changes.")
exit()

#Save (commit) the changes
conn.commit()


#Query the database
data.execute('SELECT * FROM stocks')

#Print the results
for row in data.fetchall():
    print(row)

#Clear the connection
conn.close()