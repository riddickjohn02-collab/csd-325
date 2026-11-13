
# Name: Robert Cuevas
# Date: November 10, 2026
# Assignment: CSD-325 Module 4 - Sitka Weather
# Purpose: Display high or low Sitka temperatures from a CSV file.
# Original code: sitka_highs.py, provided with the course assignment.
# Changes: Added low temperatures, a repeating menu, blue low-temperature
# graphs, input validation, an introduction, and an exit message.

import csv
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt


# Read the original data file, including high and low temperatures.
filename = Path(__file__).with_name('sitka_weather_2018_simple.csv')
dates, highs, lows = [], [], []

with open(filename, newline='', encoding='utf-8') as weather_file:
    reader = csv.reader(weather_file)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Plot the selected temperature series using the requested color.
def display_temperatures(temperatures, kind, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, color=color)

    ax.set_title(f'Daily {kind} temperatures - Sitka, 2018', fontsize=16)
    ax.set_xlabel('')
    ax.set_ylabel('Temperature (F)', fontsize=12)
    fig.autofmt_xdate()
    ax.tick_params(axis='both', which='major', labelsize=10)
    plt.show()
    plt.close(fig)


# Introduce the menu and repeat until the user chooses Exit.
def main():
    print('Sitka Weather - 2018')
    print('Choose Highs to see red high temperatures,')
    print('Lows to see blue low temperatures, or Exit to quit.')

    while True:
        print('\nMenu: Highs, Lows, Exit')
        selection = input('RC: ').strip().lower()

        if selection in ('highs', 'h'):
            display_temperatures(highs, 'high', 'red')
        elif selection in ('lows', 'l'):
            display_temperatures(lows, 'low', 'blue')
        elif selection in ('exit', 'e'):
            print('Thank you for using the Sitka Weather program. Goodbye!')
            break
        else:
            print('Invalid selection. Please choose Highs, Lows, or Exit.')


if __name__ == '__main__':
    main()
