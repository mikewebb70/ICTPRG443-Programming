"""
Program: Temperature Analysis
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
import random

# Set parameters for Gaussian distribution
MU = 25.0       # Mean temperature
SIGMA = 3.5     # Standard deviation

# Set the number of days and hours for the 2D list

DAYS = 31
HOURS = 24

# Create the 2D list of hourly temperatures
temps = []
for day in range(DAYS):
    daily_temps = []
    for hour in range(HOURS):
        # Generate random temp rounded to 1 decimal place
        temp = round(random.gauss(MU, SIGMA), 1)
        daily_temps.append(temp)
    temps.append(daily_temps)

print("Generated Temperatures:")
print(temps)
print()

# -------------------------------------------------------------------
# Part A: Calculate and display the average temperature at noon
# Note: Noon corresponds to hour index 12 (13th hour of the day)
# -------------------------------------------------------------------
noon_sum = 0
for day in temps:
    noon_sum += day[12]

noon_average = noon_sum / len(temps)
print("Average noon temperature:", noon_average)
print()

# -------------------------------------------------------------------
# Part B: Sort each day's temperatures in ascending order
# -------------------------------------------------------------------
for day in temps:
    day.sort()


# -------------------------------------------------------------------
# Part C: Binary Search Function
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
# Part D: Search for a specific temperature on the 5th day
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
# Part E: Find and display daily highs and lows
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
