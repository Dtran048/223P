#Dylan Tran
#2/8/2024
#a file that holds all the programs that are going to be called by the main file

def add_contact(contacts,/, *, id, first_name, last_name):
    """checks if the id is in the dictionary and adds if it doesn't"""
    if id in contacts:
        return "error"
    contacts[id]=[first_name, last_name]
    return first_name, last_name

def modify_contact(contacts,/, *, id, first_name, last_name):
    """checks if the id is in the dictionary and updates it if it is"""
    if id not in contacts:
        return "error"
    contacts.update({id:[first_name,last_name]})
    return first_name, last_name

def delete_contact(contacts,/, *, id):
    """checks if the id is in the dictionary and deletes it if it is"""
    if id not in contacts:
        return "error"
    f_temp = contacts[id][0]
    l_temp = contacts[id][1]
    contacts.pop(id)
    return f_temp, l_temp

def sort_contact(contacts,/):
    """sorts the dictionary and returns it"""
    return dict(sorted(contacts.items(), key = lambda x: str(x[0]) + str(x[1])))

def find_contact(contacts,/, *, find):
    """find where the keyword is in the dictionary and prints all the items with it in it under columns"""
    dupli_contact = {}
    for k in contacts.keys():
        if k == find.lower() or str(contacts[k][0]).lower() == find.lower() or  str(contacts[k][1]).lower() == find.lower():
            dupli_contact[k] = [str(contacts[k][0]), str(contacts[k][1])] 
    print(
        """
================== FOUND CONTACT(S) ==================
Last Name            First Name           Phone
==================== ==================== ============"""
    )
    for k in sort_contact(dupli_contact).keys():
        print(f'{contacts[k][1]:21}{contacts[k][0]:21}{str(k):7}')
    return dupli_contact

def print_list(contacts):
    """this function prints out a string which acts as a column header then loops through the contact list to print each one"""
    print(
        """
==================== CONTACT LIST ====================
Last Name            First Name           Phone
==================== ==================== ============"""
    )
    for k in contacts.keys():
        print(f'{contacts[k][1]:21}{contacts[k][0]:21}{str(k):7}')

