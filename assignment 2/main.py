#Dylan Tran
#2/8/2024
# acts as the main file and calls funtions from the contacts file depending on what the user requests
from contacts import *

contacts= []
acceptable_values = {'1','2','3','4','5','6','7'}
x= 0
while x != 7:
    print("""  
    *** EMPLOYEE CONTACT MAIN MENU ***
    1. Print list
    2. Add contact
    3. Modify contact
    4. Delete contact
    5. Sort list by first name
    6. Sort list by last name
    7. Exit the program
    """)
    x= 0
    while (x in acceptable_values) == False:
        x = input("Enter menu choice: ")
    x = int(x)
    if x == 1:
        print_list(contacts)
    elif x == 2:
        a = str(input("Enter First Name: "))
        b = str(input("Enter Last Name: "))
        add_contact(contacts, first_name= a, last_name = b)
    elif x == 3:
        c = int(input("Enter Index: "))
        a = str(input("Enter First Name: "))
        b = str(input("Enter Last Name: "))
        modify_contact(contacts, first_name = a, last_name = b, index= c)
    elif x == 4:
        c = int(input("Enter Index: "))
        delete_contact(contacts, index = c)
    elif x == 5:
        contacts = sort_contacts(contacts, column = 0)
    elif x == 6:
        contacts = sort_contacts(contacts, column = 1)
    else:
        break
    

