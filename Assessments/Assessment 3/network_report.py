"""
Program: network_report.py. Create and manage python lists, dictionaries and TXT file (manage network data)
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
    - Part B:   
    Generate a text report called network_report.txt with the network devices, IP addresses, network services 
     and port numbers then merge the network_report.txt with Introduction.txt
Author: Michael Webb
Student ID: 20172813
Date: 2026-11-28
Version: 1.0
"""
import os # so we can open and write files
import fileinput # so we can cleanly merge files
import tempfile # so we can 


# from network_data import network_devices_dict, network_services_ports
# NOTE: This is causing an issue with circular dependencies
# as network_data.py is imported by this script.  guarding using
# name main idiom is not preventing this script from runining
# on import.
# 

# Determine the absolute directory path where this script resides
# Thankyou reddit r/python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define file names with absolute path to the script directory
report_file = os.path.join(script_dir, "network_report.txt")
intro_file = os.path.join(script_dir, "Introduction.txt")
scratch_file = os.path.join(script_dir, "scratch.txt")

# Function to display a heading for sections of the program
def file_heading(title, file_var):
    """Write an uppercase heading and separator line to an open file."""
    file_var.write("-" * 40 + "\n")
    file_var.write(f"{title.upper()}\n")
    file_var.write("-" * 40 + "\n")

# Loading functions and data from network_data.py locally to avoid importing the entire module globally
# which was causing a circluar dependency loop. 
# https://www.datacamp.com/tutorial/python-circular-import
def create_report(devices_dict, services_dict):
    """Create a report file with the network data."""
    # Open the report file for writing using with statement for safer file handling and 
    # closing as well as better visability for Pylance LSP
    with open(report_file, "w") as file:

   #-------------------------------------------------------------------------------------------------
   # 2. Write a clear heading to the report.

        #Write Report Header
        file_heading("NETWORK REPORT", file)        
        file.write("Author: Michael Webb\n")
        file.write("Student ID: 20172813\n")
        file.write("Date: 2026-11-28\n")
        file.write("-" * 40 + "\n\n")

    #-------------------------------------------------------------------------------------------------
    #   3.	Use the network device and network service dictionaries from network_data.py to generate the report. 
    #   You should import the required dictionaries into network_report.py rather thanmanually recreating or duplicating the data. 

        # Write Network Devices Section
        file_heading("NETWORK DEVICES", file)

        for device, ip in devices_dict.items():
            file.write(f"{device} - {ip}\n")
        file.write("\n")

        # Write Network Services Section
        file_heading("NETWORK SERVICES", file)
        for service, port in services_dict.items():
            file.write(f"{service} - Port {port}\n")
        file.write("\n")

        # Write Network Summary Section
        file_heading("NETWORK SUMMARY", file)


        file.write(
            "This report contains the network device names, IP addresses,\n"
            "network services and associated port numbers.\n"
        )
        print(f"Report created successfully : {report_file}")

#-------------------------------------------------------------------------------------------------
# 6.	Merge the network_report.txt with Introduction.txt. 

# moved to setting default parameter values as named arguments to the function 
# instead of calling the function with positional argumetns with the file names/locations
def merge_files(report=report_file, intro=intro_file, scratch=scratch_file):
    """
    Copies primary_report to scratch file, then uses fileinput to merge
    intro and scratch back into primary_report.
    """
    with (
    open(report, "r") as in_file,
    open(scratch, "w") as out_file, 
    ):
     out_file.write(in_file.read()) 

    print(f"Copied {os.path.basename(report)} to {os.path.basename(scratch)}")

    # Merge the intro_file and scratch_file into report_file
    with open(report, "w") as final_report:
        for line in fileinput.input([intro, scratch]):
            final_report.write(line)

    print(f"Merged report saved to: {report}")
    
    # Clean up the scratch file
    if os.path.exists(scratch_file):
        os.remove(scratch_file)
    print(f"Cleanup scratch file {os.path.basename(scratch_file)}")

def generate_final_report():
    """ 
    Create a final report file from the primary_report and intro mergered files
    Target for user menu selection in network_data.py
    """
    # Local import prevents circular dependency and resolves the NameError
    from network_data import network_devices_dict, network_services_ports

    create_report(network_devices_dict, network_services_ports)
    merge_files()   

if __name__ == "__main__":
    # uncomment the bellow statement when this script is run directly for testing to  import network_data.py
    # 
    # from network_data import network_devices_dict, network_services_ports
    generate_final_report()
