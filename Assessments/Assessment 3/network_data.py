"""
Program:  network_data.py Create and manage python lists, dictionaries and TXT file (manage network data)
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
    - Part A:   Manage Python lists and dictionaries of network devices, IP addresses,
                    services and ports with ability to search, add, delete and sort by device or
                    service name.
Repo: https://github.com/mikewebb70/ICTPRG443-Programming/tree/main/Assessments/Assessment%203
Author: Michael Webb
Student ID: 20172813
Date: 2026-11-28
Version: 1.0
"""
# Import necessary modules
import os
import subprocess

# Import the generate_final_report function from the network_report.py script
from network_report import generate_final_report

# Function to clear the console screen, makes it easier to read the output of the programme.
def clear_screen():
    """
    Clear the terminal screen using subprocess.
    (pylint picked up on a deprecated method in the os module, 
    so I used subprocess instead)
    """
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)

# Function to display a heading for sections of the program
def heading(title):
    print("-" * 40)
    print(title)
    print("-" * 40)

# -------------------------

# 1.	Create a list that stores at least 12 network device names.
network_devices = [
    "Access Point",
    "Floor 1 Switch",
    "Floor 2 Switch",
    "Firewall",
    "Jump Box",
    "Web Server",
    "Database Server",
    "Development Server",
    "Mail Server",
    "File Server",
    "Router01",
    "Active Directory Server"
]
#-------------------------------------------------------------------------------------------------

# 2. Create a list that stores at least 12 IP address.
# The position of each IP address must correspond to the network device in the first list.
network_ip_addresses = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4", 
    "192.168.2.1",
    "192.168.2.2",
    "192.168.2.3",
    "172.16.0.4",
    "172.16.0.5",
    "172.16.0.6",
    "10.0.0.1",
    "10.40.2.16"
]
#-------------------------------------------------------------------------------------------------

# 3. Create a dictionary using the network device names (step 1) as keys
# and the corresponding IP addresses (step 2) as values.
# The dictionary must be created using the two lists from Steps 1 and 2.
def devices_and_addresses():
    """
    Create a dictionary of network devices and their IP addresses.
    The keys are the device names, and the values are the corresponding IP addresses.
    """
    return dict(zip(network_devices, network_ip_addresses))


# Create a usable object of the network devices and IP addresses dictionary
network_devices_dict = devices_and_addresses()
#-------------------------------------------------------------------------------------------------

# 4. Create a dictionary that stores at least 5 common network services
# and their associated port numbers.
network_services_ports = {
    "HTTPS": 443,
    "FTP": 21,
    "SSH": 22,
    "SMTP": 25,
    "DNS": 53,
    "RDP": 3389,
    "LDAP": 389
}

#--------------------------------------------------------------------------------------------------
# 5. Create a function which ask the user to enter a new device name and IP address,
# then add them to the network device list and dictionary.
# Required test: Provide screenshot for below test:
# Wireless Controller - 192.168.1.5
def add_network_device():
    """
    Ask the user to enter a new device name and IP address,
    then add them to the network device list and dictionary.
    """
    clear_screen()
    heading("Add Network Device")
    
    # Loop until a non-empty, unique device name is provided
    while True:
        new_device = input("Enter the device name of the new network device: ").strip()
        
        if not new_device:
            print("Device name cannot be empty. Please try again.")
            continue
            
        # Case-insensitive duplicate check
        device_duplicate = False
        for device in network_devices_dict.keys():
            if new_device.lower() == device.lower():
                print(f"Device '{device}' already exists. Please try again.")
                device_duplicate = True
                break # restart the loop to ask for a new device name
                
        if not device_duplicate:
            break  # exit loop unique device name entered

    # Loop until a non-empty IP address is provided
    while True:
        new_ip = input("Enter the IP address of the new network device: ").strip()
        
        if not new_ip:
            print("IP address cannot be empty. Please try again.")
            continue

        # Case-insensitive duplicate check
        ip_duplicate = False
        for ip in network_devices_dict.values():
            if new_ip == ip:
                print(f"IP Address '{ip}' already exists. Please try again.")
                ip_duplicate = True
                break # restart the loop to ask for a new device name
                
        if not ip_duplicate:
            break  # exit loop unique IP entered
      
    # Update both parallel lists and the dictionary together
    network_devices.append(new_device)
    network_ip_addresses.append(new_ip)
    network_devices_dict[new_device] = new_ip

    print(f"\nSuccessfully added '{new_device}' : {new_ip}")
    input("\nPress Enter to return to main menu...")
    

#-------------------------------------------------------------------------------------------------
# Functions to display network devices and services for dictionaries
def display_network_devices():
    """
    Iterate through the network devices dictionary and print each device
    and its corresponding IP address.
    """
    clear_screen()
    heading("Network Devices and IP Addresses")

    for device, ip in network_devices_dict.items():
        print(f"{device} : {ip}")
    input("\nPress Enter to return to the main menu")

def display_network_services():
    """Print each service and its corresponding port number."""
    clear_screen()
    heading("Network Services and Port Numbers")
  
    for service, port in network_services_ports.items():
        print(f"{service} : {port}")
    input("\nPress Enter to return to the main menu")
#------------------------------------------------------------------------
# 6. Create a function which ask the user to enter the name of an existing network device to delete.
# Remove the device and its corresponding IP address from the list and dictionary.
# Required test: Delete:  Printer01 – 192.168.1.20
def delete_network_device():
    """Ask user for existing device name and remove it from lists and dictionary."""
    clear_screen()
    heading("Delete Network Device")
  
    device_to_delete = input("Enter the name of the network device to delete: ").strip()
    
    # Initialise the variable so it exists even if no match is found
    matched_device = None
    
    for device in network_devices_dict.keys():
        if device_to_delete.lower() == device.lower():
            matched_device = device
            break

    if not matched_device:
        # Gracefully exit and inform the user that the device does not exist
        print(f"\nDevice '{device_to_delete}' not found in the network records.")
        input("Press Enter to return to the main menu.")
    else:
        print(f"Deleting {matched_device}.")
        input("Press Enter to confirm deletion.")
        # Remove from dictionary and retrieve its IP
        ip_address = network_devices_dict.pop(matched_device)
        # Remove from lists
        network_devices.remove(matched_device)  
        # Remove the corresponding IP address from the list
        network_ip_addresses.remove(ip_address)
        input(f"{matched_device} with IP address {ip_address} deleted. \n \npress Enter to return to the main menu.")

#-------------------------------------------------------------------------------------------------

# 7. Create a function which allows the user to choose what data to sort:
#   Network devices: Sort alphabetically by device name.
#   Network services: Sort alphabetically by service name.
# Display the sorted results.
def sort_menu():
    """Allow user to select which data structure to sort and display."""
    while True:
        clear_screen()
        heading("Sort Options")
        print("1. Sort Network Devices (Alphabetically by Name)")
        print("2. Sort Network Services (Alphabetically by Service Name)")
        print("3. Return to Main Menu")
        choice = input("\nEnter choice (1, 2 or 3): ").strip()
        if choice == '1':
            clear_screen()
            heading("Sorted Network Devices")
            sorted_devices = dict(sorted(network_devices_dict.items()))
            for device, ip in sorted_devices.items():
                print(f"{device} : {ip}")
            input("\nPress any key to retern to menu.")
            break
        elif choice == '2':
            clear_screen()
            heading("Sorted Network Services")
            sorted_services = dict(sorted(network_services_ports.items()))
            for service, port in sorted_services.items():
                print(f"{service} : Port {port}")
            input("\nPress any key to return to menu.")
            break    
        elif choice == '3':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            input("\nPress Enter to try again.")
            continue
#-------------------------------------------------------------------------------------------------

# 8. Create a function which allows the user to choose what data to search:
#   Network devices: Search by device name and display its IP address.
#   Network services: Search by service name and display its port number.
def search_network_device():
    """
    Search for a network device by name and display its IP address.
    """
    clear_screen()
    heading("Search Network Device")
    search_term = input("Enter the name of the network device to search for: ").strip()
    found = False
    for device, ip in network_devices_dict.items():
        if search_term.lower() == device.lower():
            print(f"\nExact match found:\n{device} : {ip}")
            found = True
            break
        elif search_term.lower() in device.lower():
            print(f"\nPartial match found:\n{device} : {ip}")
            found = True
    if not found:
        print(f"\nDevice '{search_term}' not found in the network records.")
  #  input("\nPress Enter to return to the main menu")

def search_network_service():
    """
    Search for a network service by name and display its port number.
    """
    clear_screen()
    heading("Search Network Service")
    search_term = input("Enter the name of the network service to search for: ")
    found = False
    for service, port in network_services_ports.items():
        if search_term.lower() in service.lower():
            print(f"\nService found:\n{service} :Port {port}")
            found = True
            break
        elif search_term.lower() in service.lower():
            print(f"\nPartial match found:\n{service} : Port {port}")
            found = True
    if not found:
        print(f"\nService '{search_term}' not found in network service records.")
    #input("\nPress Enter to return to the main menu")

def search_menu():
    """Allow user to select which data structure to search."""
    while True:
        clear_screen()
        heading("Search Options")
        print("1. Search Network Devices")
        print("2. Search Network Services")
        print("3. Return to Main Menu")
        choice = input("\nEnter choice (1, 2, or 3): ").strip()
        if choice == '1':
            search_network_device()
            input("\nPress Enter to return to the search menu")
        elif choice == '2':
            search_network_service()
            input("\nPress Enter to return to the search menu")
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")
            input("\nPress Enter to try again.")

#-------------------------------------------------------------------------------------------------

def generate_report_option():
    """ Menu option for Part B report creation"""
    clear_screen
    heading("Create Network Report")
    generate_final_report()
    input("\nPress Enter to return to the main menu")

#-------------------------------------------------------------------------------------------------

def menu():
    """main menu display."""
    heading("Main Menu")
    print("1. Add Network Devices and IP Addresses")
    print("2. Delete a Network Device")
    print("3. Sort Network Devices or Services")
    print("4. Search Network Devices or Services")
    print("5. Display ALL Network Devices and IP Addresses")
    print("6. Display ALL Network Services and Port Numbers")
    print("7. Create Network Report")
    print("\n8. Exit Programme")
    print("-" * 40 )

# Menu Selection
def main():
    """
    Main program loop to display the menu and handle user input for  network data  tasks.
    """
    while True:
        clear_screen()
        menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == '1':
            add_network_device()
        elif choice == '2':
            delete_network_device()
        elif choice == '3':
            sort_menu()
        elif choice == '4':
            search_menu()
        elif choice == '5':
            display_network_devices()
        elif choice == '6':
            display_network_services()
        elif choice == '7':
            generate_report_option()
        elif choice == '8':
            clear_screen()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            input("Press Enter to continue.")

if __name__ == "__main__":
    main()  # Start the program
