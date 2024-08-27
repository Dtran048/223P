#Dylan Tran
#3/7/2024
# acts as the main file and calls funtions from the contacts file depending on what the user requests
from contacts import *


acceptable_values = {'1','2','3','4','5','6'}
x= 0
addcin = Contacts(filename="defafil")

while x != 6:
    print("""  
    *** TUFFY TITAN WEATHER LOGGER MAIN MENU ***
    1. Add contact
    2. Modify contact
    3. Delete contact
    4. Print contact list
    5. Set contact filename
    6. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        # ask foir valid input
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        # ask for id and full name then calls addcontact and if error tells why
        a = str(input("Enter id: "))
        b = str(input("Enter first name: "))
        c = str(input("Enter last name: "))
        result = addcin.add_contact(id=a, first_name=b, last_name=c)
        if (result) == "error":
            print("id already exist")
        else:
            print(result)
    elif x == 2:
        # ask for id and full name then calls modify_contact and if error tells why
        a = str(input("Enter id: "))
        b = str(input("Enter first name: "))
        c = str(input("Enter last name: "))
        result = addcin.modify_contact(id=a, first_name=b, last_name=c)
        if (result) == "error":
            print("id doesn't exist")
        else:
            print(result)
    elif x == 3:
        # ask for id and full name then calls modify_contact and if error tells why
        a = str(input("Enter id: "))
        result = addcin.delete_contact(id = a)
        if (result) == "error":
            print("id doesn't exist")
        else:
            print(result)
    elif x == 4:
        # calls print_dic
        addcin.print_dic()
    elif x == 5:
        # asks for user to input a file name and sets that to the default
        a = str(input("Enter filename: "))
        addcin = Contacts(filename=a)
    else:
        break
