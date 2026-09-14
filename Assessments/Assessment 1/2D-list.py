"""
Program: Temperature Analysis
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Create a 2D list of hourly temperatures for a 31 day month then
             - calculate the noon average, 
             - sort daily temperatures,
             - perform a binary search,
             - find daily high/low temperatures.
             
Author: Michael Webb
Student ID: 20172813
Date: 2026-09-10
Version: 1.0
"""


# Import the random module to generate random temperatures using a Gaussian distribution.
# https://www.geeksforgeeks.org/python/random-gauss-function-in-python/
import random

# Set global variables for Gaussian distribution
MU = 25.0       # Mean temperature
SIGMA = 3.5     # Standard deviation

# Set global variables for the number of days and hours for the 2D list
DAYS = 31
HOURS = 24

""" Create the 2D list of hourly temperatures """
# Create empty lists to hold the temperatures.
temps = []
daily_temps = []
# This for loop creates a list of 31 (DAYS) lists, each containing 24 (HOURS) random temperatures.
for day in range(DAYS):
    # This for loop creates a list of 24 (HOURS) random temperatures for each DAY. 
    for hour in range(HOURS):
        # Generate random temp rounded to 1 decimal place.
        # round is a built in function.
        temp = round(random.gauss(MU, SIGMA), 1)
        # .append is a method from the built in list function.
        daily_temps.append(temp)
    temps.append(daily_temps)

print("Generated Temperatures:")
print(temps)
print()

# -------------------------------------------------------------------
# a)Write code to display the average temperature at noon 
# -------------------------------------------------------------------
noon_sum = 0
for day in temps:
    noon_sum += day[12]

noon_average = noon_sum / len(temps)
print("Average noon temperature:", noon_average)
print()

# -------------------------------------------------------------------
# b) Sort the existing array of daily temps in ascending order 
# (hint: use Python’s built in sort() method)
# -------------------------------------------------------------------
for day in temps:
    day.sort()


# -------------------------------------------------------------------
# c) Code your own binary search algorithm as a new function defined as follows 
# (hint: many examples available online). Also write a comment just above 
# the function definition with a short description of how it works.
# -------------------------------------------------------------------
def binary_search(array, item):
    """
    https://www.w3schools.com/Python/python_dsa_binarysearch.asp
    Binary search finds an item in a sorted list by repeatedly dividing
    the search interval in half until the target is found or bounds cross.
    
    Args:
        array: A sorted list to search in.
        item: The value to search for.
    
    Returns:
        True if the item is found, False otherwise.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == item:
            return True  # Item found
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return False  # Item not found


# -------------------------------------------------------------------
# d) Use your binary search to find out if the 5th day recorded a specific temp 
# (eg. 21.1 degrees; pick your own value)
# Note: The 5th day is at index 4
# -------------------------------------------------------------------
DAY_FIVE = temps[4]

# Choose a sample target temperature to search for
TARGET_TEMP = 18.8

FOUND = binary_search(DAY_FIVE, TARGET_TEMP)

if FOUND:
    print(f"Temperature {TARGET_TEMP}°C was recorded on Day 5.")
else:
    print(f"Temperature {TARGET_TEMP}°C was NOT recorded on Day 5.")

print(f"Day 5 temperatures (sorted): {DAY_FIVE}")
print()

# -------------------------------------------------------------------
# e) Print two lists, one showing all the daily highs and another the daily lows.
# -------------------------------------------------------------------
lows = []
highs = []

for day in temps:
    # each day is sorted in ascending order,
    # the 1st element (index 0) is the min, and the last (index -1) is the max.
    lows.append(day[0])
    highs.append(day[-1])

print("Lows:", lows)
print("Highs:", highs)
