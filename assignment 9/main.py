from flights import *

acceptable_values = {'1','2','3','4'}
x = 0
insobj = Flights("default")
while x != 4:
    print("""  
    *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU
1. Add flight
2. Print flight schedule
3. Set flight schedule filename
4. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        # ask for valid input
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        a = str(input("Enter origin: "))
        b = str(input("Enter destination: "))
        c = str(input("Enter flight number: "))
        d = str(input("Enter departure time (HHMM): "))
        e = str(input("Enter arrival time (HHMM): "))
        f = str(input("Is arrival next day (Y/N): "))
        while (f != "Y") and (f != "N"):
            f = str(input("Is arrival next day (Y/N): "))
        insobj.add_flight(a,b,c,d,f, e)
    elif x == 2:
        print("""
================== FLIGHT SCHEDULE ==================
Origin Destination Number Departure Arrival Duration
====== =========== ====== ========= ======== ========"""
        )
        g = insobj.get_flights()
        for i in g:
            print(f'{i[0]:7}{i[1]:12}{i[2]:>6}{i[3]:>10}{i[5]:>9}{i[4]:>9}') 
    elif x == 3:
        flightfile = str(input("Enter data filename: "))
        insobj = Flights(flightfile)
    else:
        break
