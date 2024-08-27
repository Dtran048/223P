#Dylan Tran
#2/4/2024
#a python program that performs as a employee contact list


def print_list(contacts):
    """this function prints out a string which acts as a column header
       then loops through the contact list to print each one"""
    print(
        """
============== CONTACT LIST ==============
Index   First Name          Last Name
==========================================
        """
    )
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts):
    """this function asks for the user to input the first and then last name
       where it will then append the name in a list and theh append that list into the 
          main contact list"""
    name = []
    print("Enter the first name: ", end="")
    name.append(input())
    print("Enter the last name: ", end="")
    name.append(input())
    contacts.append(name)
    return contacts

def modify_contact(contacts):
    """this function asks for the list index and sees if it a vaild one where it will 
       then ask for the first and last name where it will then replace the name in the spot """
    x = int(input("Enter the List index number: "))
    if x < 0 or x > len(contacts):
        print("Invalid Index Number.")
        return
    print("Enter the first name: ", end="")
    contacts[x][0] = input()
    print("Enter the last name: ", end="")
    contacts[x][1] = input()
    return contacts

def delete_contact(contacts):
    """this functions asks for the index number while looking if the number is valid
       then it deletes the contact in the spot"""
    x = int(input("Enter the index number of the list you would like to delete: "))
    if (x < 0) or (x > len(contacts)):
        print("Invalid Index Number.")
        return
    del contacts[x]
    return contacts
 
