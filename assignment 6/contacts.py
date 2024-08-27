import json 

class Contacts:
    # sets the filename, create an empty dictionary and loads the file if it exists
    def __init__(self, /, *, filename):
        self.file = filename
        self.dictitem = {}
        try:
            with open(self.file, 'r') as f:
                self.dictitem = json.load(f)
        except FileNotFoundError:
            return
    
    # checks if id is in it then adds sorts, and stores the dictionary
    def add_contact(self, /, *, id, first_name, last_name):
        if id in self.dictitem:
              return("error")
        self.dictitem[id] = [first_name,last_name] 
        self.dictitem = dict(sorted(self.dictitem.items(), key=lambda item:  (item[1][1] + item[1][0])))
        with open(self.file, "w") as outfile:
            json.dump(self.dictitem, outfile)
        item = f'{id} : {self.dictitem[id]}'
        return(item)

    # checks if id is in it then modify, sorts, and stores the dictionary
    def modify_contact(self, /, *, id, first_name, last_name):
        if id not in self.dictitem:
              return("error") 
        self.dictitem[id] = [first_name,last_name]
        self.dictitem = dict(sorted(self.dictitem.items(), key=lambda item: (item[1][1] + item[1][0]) ))
        with open(self.file, "w") as outfile:
            json.dump(self.dictitem, outfile)
        item = f'{id} : {self.dictitem[id]}'
        return(item)

    # checks if id is in it then stores it for a short time, and deletes it 
    def delete_contact(self, /, *, id):
        if id not in self.dictitem:
            return("error") 
        name = self.dictitem[id]
        del self.dictitem[id]
        with open(self.file, "w") as outfile:
            json.dump(self.dictitem, outfile)
        item = f'{id} : {name}'
        return(item)

    # prints the dictionary
    def print_dic(self):
        print(
        """
==================== CONTACT LIST ====================
Last Name            First Name           Id
==================== ==================== =========="""
        )
        for i in self.dictitem:
            print(f'{self.dictitem[i][1]:21}{self.dictitem[i][0]:21}{str(i):7}')