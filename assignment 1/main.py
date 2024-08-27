#Dylan Tran
#2/4/2024
# implement a menu and import the contacts module
from contacts import *


contacts= []
x=0
while x != 5:
    print("""  
    *** EMPLOYEE CONTACT MAIN MENU ***
    1. Print list
    2. Add contact
    3. Modify contact
    4. Delete contact
    5. Exit the program
    """)
    x = int(input("Enter menu choice: "))
    if x == 1:
        print_list(contacts)
    elif x == 2:
        add_contact(contacts)
    elif x == 3:
        modify_contact(contacts)
    elif x == 4:
        delete_contact(contacts)
    else:
        break
    

