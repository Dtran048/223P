#Dylan Tran
#3/7/2024
# acts as the main file and calls funtions from the weather file depending on what the user requests
from weather import *

weatherfile = ""

weatherday = {}
acceptable_values = {'1','2','3','4','5'}
x= 0


while x != 6:
    print("""  
    *** TUFFY TITAN WEATHER LOGGER MAIN MENU ***
    1. Set data filename
    2. Add weather data
    3. Print daily report
    4. Print Historical report
    5. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        # calls for a filename and saves it
        weatherfile = str(input("Enter data filename: "))
        weatherday = read_data(filename = weatherfile)
    elif x == 2:
        #asks user for info and checks if it is valid
        a = str(input("Enter date (YYYYMMDD): "))
        while len(a) != 8 or a.isdigit() == False:
            a = str(input("Enter valid date (YYYYMMDD): "))
        b = str(input("Enter time (hhmmss): "))
        while len(b) != 6 or b.isdigit() == False:
            b = str(input("Enter valid time (hhmmss): "))

        c = str(input("Enter temperature: "))
         
        while ((c.isdigit() == False) and (c[0] == "-" and c[1:].isdigit() == True) == False):
            c = str(input("Enter valid temperature: "))

        d = str(input("Enter humidity: "))
        while ((d.isdigit() == False) and (d[0] == "-" and d[1:].isdigit() == True) == False):
            d = str(input("Enter vaild humidity: "))
        x = 0
        e = str(input("Enter rainfall: "))
        while x == 0:
            try:
                float(e)
                x = 5
            except ValueError:
                e = str(input("Enter valid rainfall: "))
        a = a + b
        weatherday[a+b] = {'t': int(c), 'h': int(d), 'r': float(e)} 
        write_data(filename = weatherfile, data = weatherday)
    elif x == 3:
        #ask for date and calls the report daily function
        a = 0
        a = str(input("Enter date (YYYYMMDD): "))
        while len(a) != 8 and a.isdigit() == True:
            a = str(input("Enter valid date (YYYYMMDD): "))
        report_daily(data = weatherday, date = a)
    elif x == 4:
        #calls the report historical function
        report_historical(data = weatherday)
    else:
        break
    

