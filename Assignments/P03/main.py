###############################################################################
#
#  Author:           Rykir Evans
#  Email:            rjevans0408@my.msutexas.edu | rykirjoe@yahoo.com
#  Title:            Pet Daycare Database
#  Course:           CMPS 4143 Java and Python
#  Professor:        Dr. Tina Johnson
#  Semester:         Fall 2025
#
#  Description:
#         This program manages a simple database in the form of a Python
#         list composed of dictionaries, where each entry contains a name,
#         species, and preferences of the pet. 5 Options are laid out for
#         the user to view/edit the database.
#         
#  Usage:
#         To use this program, use some standard Python interpreter and run 
#         executable. You will be prompted to enter the number corresponding
#         to one of 5 choices where you can then view/edit database entries.
#         The program stops once you select option 5.
#         
#  Files: 
#         main.py
###############################################################################

def addNew(petDB):
    print("")

    # Variable collection
    name = input("Please enter the name of the pet: ")
    species = input ("Please enter the species of the pet: ")
    pref = input("Please enter any special preferences of the pet: ")

    # Creation of dictionary and addition to list
    petDB.append({"Name": name, "Species": species, "Preferences": pref})

    print("Pet successfully added!\n")

def viewPets(petDB):
    print("")
    # Print each dictionary within the list
    for i in petDB:
        print(i)
    print("")

def updatePetPref(petDB):
    print("")
    # Search variables
    nameSearch = input("Please enter the name of the pet: ")

    # Tracker for deterministic output
    count = 0

    # Main loop for search
    for i in petDB:
        # If found, ask if it is the correct one
        if i["Name"].lower() == nameSearch.lower():
            count += 1
            print(i)
            ans = input("Is the listed pet the one whose preferences you wish to modify? y/n: ")

            # If modifying, update appropriate variables
            if ans == "y":
                updatePref = input("Please enter the updated preference(s): ")
                i["Preferences"] = updatePref
                print("Preference Updated")
                count = -1
            # Search further if the user said it was incorrect
            else:
                print("Okay, continuing to search...")

    # Determine output
    if count == 0:
        print("No matching entry found\n")
    elif count >= 1:
        print("End of database reached, no further matches identified...\n")
    else:
        print("")
    


def searchSpec(petDB):
    print("")
    # Prompt user
    search = input("Please enter the species you are searching for: ")

    # Print every entry matching the search
    for i in petDB:
        if i["Species"].lower() == search.lower():
            print(i)
    print("")
        
############
### MAIN ###
############

# Initial Output and options
print("Rykir Evans\nCMPS 4143 - Java and Python")
print("Dr. Johnson\nPet Daycare Database\n")
print("Please choose from the following options:")
print("1. Add new pet")
print("2. View all pets")
print("3. Update pet preference")
print("4. Search pets by species")
print("5. Exit the database")

choice = input()

# Initial databse entries for testing
database = [
    {"Name": "Bella", "Species": "Dog", "Preferences": "Belly Rubs"},
    {"Name": "Polly", "Species": "Parrot", "Preferences": "Cursing"},
    {"Name": "Bufor", "Species": "Dog", "Preferences": "Barking"},
]

# Main loop
while not choice == "5":
    # Switch case for respective function call
    match choice:
        case "1":
            addNew(database)
        case "2":
            viewPets(database)
        case "3":
            updatePetPref(database)
        case "4":
            searchSpec(database)
        # Default case by using wildcard regex
        case _:
            print("Invalid choice, please try again.")
    # Re-enter the next choice
    choice = input("Please enter your next action 1-5: ")

print("Exiting, goodbye.")