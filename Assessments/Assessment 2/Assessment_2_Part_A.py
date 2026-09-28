
"""
Program: Python Lists and Dictionaries (manage a collection of favourites)
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
             - Part A: Manage Python lists for favourite actors, movies, and games
               with ability to search, add, delete and sort.
             - Part B: Manage Python dictionaries storing favourites pairing additional data
               (birthdays and release years) with corresponding manipulation features.

Author: Michael Webb
Student ID: 20172813
Date: 2026-09-28
Version: 1.0
"""

#-----------------------------------------------------------------------------

"""
Part A
In the first part of this assessment, you must design, code, and test a program that uses a Python list data structure.
Use the following scenario:
1.	A list that stores at least 12 of your favourite actors/actresses’ names.
2.	A list that stores at least 12 of your favourite movies.
3.	A list that stores at least 12 of your favourite games.
4.	Write a Python program that provides the ability to:
4.1.	Create a list from scenario above
4.2.	Add a value to the list
4.3.	Delete a value from the list
4.4.	Sort all the data in the list in the ascending order. Sort all the data in the list in the descending order.
4.5.	Search for the value in the list asking user for input.
5.	Debug and test your program. You must conduct program tests to test the functionality specified above
"""

import os

# 1. A list that stores at least 12 of your favourite actors/actresses’ names.
actors = [
        "Tom Hardy",
        "Jake Gyllenhaal",
        "Denzel Washington",
        "Scarlett Johansson",
        "Leonardo DiCaprio",
        "Nicole Kidman",
        "Morgan Freeman",
        "Cate Blanchett",
        "Brad Pitt",
        "Helen Mirren",
        "Keanu Reeves",
        "Emma Stone"
    ]

# 2. A list that stores at least 12 of your favourite movies
movies = [
        "Star Wars",
        "Resident Evil",
        "The Dark Knight",
        "Pulp Fiction",
        "Forrest Gump",
        "Interstellar",
        "Gladiator",
        "The Matrix",
        "Superman",
        "Jurassic Park",
        "Avatar",
        "The Avengers"
    ]

# 3. A list that stores at least 12A list that stores at least 12 of your favourite games
games = [
        "Defender",
        "Sid Meier’s Civilization",
        "Tetris",
        "The Legend Of Zelda",
        "SimCity",
        "Diablo",
        "Super Mario",
        "Halo",
        "Doom",
        "Quake",
        "Gears of War",
        "Team Fortress"
    ]

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
# 4.
def main_menu():
    print("\n****  Menu  ****\n")
    print("1. Display List")
    print("2. Add a Favorite")
    print("3. Delete a Favorite")
    print("4. Sort List (Ascending)")
    print("5. Sort List (Descending)")
    print("6. Search Favorites")
    print("\n7. Exit Programme")
    print("****************\n")

def list_menu():
    while True:
        clear_screen()
        print("\n****  Available List  ****\n")
        print("1. Actors List")
        print("2. Movies List")
        print("3. Games List")
        print("4. Return to main Menu")
        print("****************************\n")

        list_choice = input("Enter your list choice (1-4): ")
        # List Selection
        if list_choice == '1':
            return actors, "Actors"
        elif list_choice == '2':
            return movies, "Movie"
        elif list_choice == '3':
            return games, "Games"
        elif list_choice == '4':
            print("Returning to Main Menu")
            return None, None
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            input("Press Enter to continue.")

def view_list():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Displaying {selected_name} list")
        print("----------------------------------")
        for item in selected_list:
            print(item)
        print("----------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def sort_list():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Sorting {selected_name} list")
        print("----------------------------------")
        selected_list.sort()
        for item in selected_list:
            print(item)
        print("----------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def sort_list_desc():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Sorting {selected_name} list")
        print("----------------------------------")
        selected_list.sort(reverse=True)
        for item in selected_list:
            print(item)
        print("----------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def search():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Searching {selected_name} list")
        print("----------------------------------")
        search_term = input("Search for a favorite: ")
        found = False
        for item in selected_list:
            if search_term.lower() in item.lower():
                print(item)
                found = True
        if not found:
            print("No matching items found.")
        print("----------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def add_favorite():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Adding {selected_name} to favorites")
        print("----------------------------------")
        favorite = input("Enter favorite item: ")
        selected_list.append(favorite)
        print(f"{favorite} added to favorites.")
        print("----------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def delete_favorite():
    clear_screen()
    selected_list, selected_name = list_menu()
    if selected_list is not None:
        print("----------------------------------")
        print(f"Deleting {selected_name} from favorites")
        print("----------------------------------")
        favorite = input("Enter favorite item to delete: ")
        if favorite in selected_list:
            selected_list.remove(favorite)
            print(f"{favorite} deleted from favorites.")
        else:
            print(f"{favorite} not found in favorites.")
        print("----------------------------------")


 # Menu Selection
while True:
    clear_screen()
    main_menu()
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        print("Select list to display: ")
        view_list()
    elif choice == '2':
        add_favorite()
    elif choice == '3':
        delete_favorite()
    elif choice == '4':
        sort_list()
    elif choice == '5':
        sort_list_desc()
    elif choice == '6':
        search()
    elif choice == '7':
        print("exiting program. goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        input("Press Enter to continue.")
        continue

#-----------------------------------------------------------------------------
