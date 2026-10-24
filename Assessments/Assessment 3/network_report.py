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
# Import dictionaries from Part A script
from network_data import network_devices_dict, network_services_ports

# Determine the absolute directory path where this script resides
# Thankyou reddit r/python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define file names with absolute path in the script directory
report_file = os.path.join(script_dir, "network_report.txt")
intro_file = os.path.join(script_dir, "Introduction.txt")
scratch_file = os.path.join(script_dir, "scratch.txt")

# Function to display a heading for sections of the program
def file_heading(title):
    """Write an uppercase heading and separator line to an open file."""
    file.write("-" * 40 + "\n")
    file.write(f"{title.upper()}\n")
    file.write("-" * 40 + "\n")




# Import dictionaries from Part A script
from network_data import network_devices_dict, network_services_ports

file = open(report_file, "w" )
#Write Report Header
file_heading("NETWORK REPORT")        
file.write("Author: Michael Webb\n")
file.write("Student ID: 20172813\n")
file.write("Date: 2026-11-28\n")
file.write("-" * 40 + "\n\n")

# Step 3a: Write Network Devices Section
file_heading("NETWORK DEVICES")

for device, ip in network_devices_dict.items():
    file.write(f"{device} - {ip}\n")
file.write("\n")

# Write Network Services Section
file_heading("NETWORK SERVICES")
for service, port in network_services_ports.items():
    file.write(f"{service} - Port {port}\n")
file.write("\n")

# Write Network Summary Section
file_heading("NETWORK SUMMARY")

file.write(
        "This report contains the network device names, IP addresses,\n"
        "network services and associated port numbers.\n"
    )
file.close()

print(f"Report created successfully : {report_file}")

def merge_files(report, scratch, intro):
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


# Execute merge process
merge_files(report_file, scratch_file, intro_file)

