#Dylan Tran
#2/8/2024
# acts as the main file and calls funtions from the contacts file depending on what the user requests
from contacts import *

contacts= {}
acceptable_values = {'1','2','3','4','5','6'}
x= 0
while x != 6:
    print("""  
    *** EMPLOYEE CONTACT MAIN MENU ***
    1. Add contact
    2. Modify contact
    3. Delete contact
    4. Print contact list
    5. Find contact
    6. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        a = str(input("Enter phone number: "))
        b = str(input("Enter First Name: "))
        c = str(input("Enter Last Name: "))
        res = add_contact(contacts, id = a, first_name= b, last_name = c)
        if  res == "error":
            print("Phone number already exists.")
        else:
            print("Added:", res[0], res[1])
    elif x == 2:
        a = str(input("Enter phone number: "))
        b = str(input("Enter First Name: "))
        c = str(input("Enter Last Name: "))
        res = modify_contact(contacts, id = a, first_name= b, last_name = c)
        if  res == "error":
            print("Phone number does not exist.")
        else:
            print("Modified:", res[0], res[1])
    elif x == 3:
        a = str(input("Enter phone number: "))
        res = delete_contact(contacts, id = a)
        if res == "error":
            print("Invalid phone number.")
        else:
            print("Deleted:", res[0], res[1])
    elif x == 4:
        print_list(contacts)
    elif x == 5:
        d = str(input("Enter Search string: "))
        find_contact(contacts, find = d)
    else:
        break
    

