#Dylan Tran
#2/8/2024
#a file that holds all the programs that are going to be called by the main file

def add_contact(contacts,/, *, first_name, last_name):
    """adds the contact to the list using data from when the function was called"""
    name = [first_name, last_name]
    contacts.append(name)
    return contacts

def modify_contact(contacts,/, *, first_name, last_name, index):
     """modifies a contact from the list using data from when the function was called while checking if it is in range"""
     if index < 0 or index > len(contacts):
        print("Invalid Index Number.")
        return False
     contacts[index][0] = first_name
     contacts[index][1] = last_name
     return True

def delete_contact(contacts,/, *, index):
    """deletes a contact from the list while checking if it is in range"""
    if index < 0 or index > len(contacts):
        print("Invalid Index Number.")
        return False
    del contacts[index]
    return True

def print_list(contacts):
    """this function prints out a string which acts as a column header then loops through the contact list to print each one"""
    print(
        """
============== CONTACT LIST ==============
Index   First Name          Last Name
==========================================
        """
    )
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')



def sort_contacts(contacts,/, *, column):
    """sees how the user wants to order the list and oprganizes it"""
    new_contact= sorted(contacts, key=lambda x:x[column])
    return new_contact
