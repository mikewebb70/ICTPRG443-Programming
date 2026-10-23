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
import os


# Function to display a heading for sections of the program
def file_heading(title):
    """Write an uppercase heading and separator line to an open file."""
    file.write(f"{title.upper()}\n")
    file.write("-" * 40 + "\n")

output_filename = "network_report.txt"


# Import dictionaries from Part A script
from network_data import network_devices_dict, network_services_ports

with open(output_filename, "w" ) as file:
    #Write Report Header
    file_heading("NETWORK REPORT")        
    file.write("Author: Michael Webb\n")
    file.write("Student ID: 20172813\n")
    file.write("Date: 2026-11-28\n\n")

    # Step 3a: Write Network Devices Section
    file.write("NETWORK DEVICES\n")
    file.write("=" * 15 + "\n")
    # Uses left-aligned string formatting (<25) for clean alignment
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

    print(f"Report created successfully : {output_filename}")
