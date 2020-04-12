import json
import io
import os


class MyPy:

    def __init__(self):
        #initialize empty dictionary
        self.users={}
        #initialize empty list
        self.users_data = []

        # start program with prompts
        self.prompt()

    # read from json
    def read_json(self):
        with open('usersdata.json') as json_file:
            self.users_data = json.load(json_file)

    # write to json
    def write_json(self):
        with open('usersdata.json', 'w') as json_file:
            json.dump(self.users_data, json_file, indent=4)

    def prompt(self):
        print("#########################\nMYPY PHONE BOOK\n#########################")
        print("Press 1: Add New Entry\nPress 2: Delete Entry\nPress 3: Update Entry\nPress 4: Lookup Number\nPress 5: QUIT\n")
        try:
            welcome_prompt = int(input(">> "))
        except ValueError:
            print("\nPlease choose 1, 2, 3, 4 or 5\n")
            self.prompt()
        if (welcome_prompt == 1):
            self.add_entry()
        elif (welcome_prompt == 2):
            self.delete_entry()
        elif (welcome_prompt == 3):
            self.update_entry()
        elif (welcome_prompt == 4):
            self.lookup_number()
        elif (welcome_prompt == 5):
            quit()
        else:
            print("\nPlease choose 1, 2, 3, 4 or 5\n")
            self.prompt()

    def add_entry(self):
        # get current directory
        currentDirectory = os.getcwd()
        # store file name in a variable
        file_name = r'\\usersdata.json'
        # full path of json file
        total_path = currentDirectory + file_name
        # check if json file exists
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
            # access json file
            self.read_json()
            fullname = input("\nEnter Full Name: ").lower()
            try:
                phone_number = int(input("Enter Phone Number: "))
            except ValueError:
                print("\nOnly numbers allowed!")
                return self.add_entry()
            if phone_number in ([sub['phone_number'] for sub in self.users_data]):
                print("\nPhone Number already exists\n")
                return self.add_entry()
            else:
                user = {"fullname": fullname, "phone_number": phone_number}
                # add new user details to array
                self.users_data.append(user)
                # update json file with new data
                self.write_json()
                # successful message
                name = user["fullname"]
                print(f"\nEntry added successfully! New entry is: {name}\n")
                self.prompt()
        else:
            print("Unsuccessful! Either file is missing or not readable, creating file...")
            self.write_json()
            print("\nSuccessfully created file. Run app again and press 1 to add new entry.")
            self.prompt()
    
    def delete_entry(self):
        # access json file
        with open('usersdata.json') as json_file:
            self.users = json.load(json_file)
        # boolean that indicates if a value is found in the list or not
        entry_availability = False
        # get entry to be deleted
        try:
            del_number = int(input("Enter number to be deleted: "))
        except ValueError:
            print("\nOnly numbers allowed!")
            return self.delete_entry()
        for key in range(len(self.users)):
            if self.users[key]["phone_number"] == del_number:
                del self.users[key]

                # update json file
                with open('usersdata.json', 'w') as json_file:
                    json.dump(self.users, json_file, indent=4)

                # set boolean to True
                entry_availability = True
            else:
                pass
        if entry_availability == True:
            print("\nEntry deleted successfully!\n")
            self.prompt()
        else:
            print("\nName or Number does not exist!\n")
            self.prompt()


    def update_entry(self):
        # access json file
        self.read_json()
        # boolean that indicates if a value is found in the list or not
        entry_availability = False
        # get entry to be updated
        name = input("\nEnter name to be updated: ")
        try:
            number = int(input("Enter number to be updated: "))
        except ValueError:
            print("\nOnly numbers allowed!")
            return self.update_entry()

        # traverse through json file
        for key in range(len(self.users_data)):
            if self.users_data[key]["fullname"] == name and self.users_data[key]["phone_number"] == number:
                new_name = input("\nEnter new name: ")
                try:
                    new_number = int(input("Enter new number: "))
                except ValueError:
                    print("\nOnly numbers allowed!")
                    return self.update_entry()
                # assign new details to instances
                self.users_data[key]["fullname"] = new_name
                self.users_data[key]["phone_number"] = new_number

                # update json file with new data
                self.write_json()

                entry_availability = True
            else:
                # pass so that it does not end after getting the first key
                pass
        if entry_availability == True:
            print("\nEntry updated successfully!\n")
            self.prompt()
        else:
            print("\nName or Number does not exist")
            self.prompt()

    def lookup_number(self):
        # access json file
        self.read_json()
        # boolean that indicates if a value is found in the list or not
        entry_availability = False
        # enter number to lookup
        try:
            number = int(input("\nEnter number to lookup: "))
        except ValueError:
            print("\nOnly numbers allowed!")
            return self.lookup_number()
        # traverse through json file
        for key in range(len(self.users_data)):
            if self.users_data[key]["phone_number"] == number:
                found_number = self.users_data[key]["phone_number"]
                found_name = self.users_data[key]["fullname"]
                print(f"\nName is: {found_name}\nNumber is: {found_number}")
            
                # update json file with new data
                self.write_json()
                # set boolean to True
                entry_availability = True
            else:
                pass
        if entry_availability == True:
            print("\nEntry lookup successful!\n")
            self.prompt()
        else:
            print("\nName or Number does not exist! Press 1 to add new entry\n")
            self.prompt()


        

#creating an object of class:
s = MyPy()

if __name__ == "__main__":
    import sys
    