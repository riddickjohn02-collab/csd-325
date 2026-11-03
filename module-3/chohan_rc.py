# Name: Robert Cuevas
# Date: November 3, 2026
# Assignment: Module 3 - Brownfield + Flowchart(s)
# Purpose: Modify the Cho-Han game to use an RC prompt, a 12% house fee,
# and a 10 mon bonus when the dice total is 2 or 7.
# Source: Al Sweigart, The Big Book of Small Python Projects
# https://nostarch.com/big-book-small-python-projects

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random
import sys


JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}


print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

If the total of the dice roll is 2 or 7, you receive a 10 mon bonus.
''')


purse = 5000

while True:  # Main game loop.
    # Place your bet.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        # Changed the input prompt to the student's initials.
        pot = input('RC: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice and calculate the total.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_total = dice1 + dice2

    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han.
    while True:
        bet = input('RC: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # New assignment requirement: award a 10 mon bonus for a total of 2 or 7.
    if roll_total == 2 or roll_total == 7:
        print('The total of the roll was', roll_total,
              'and you received a 10 mon bonus!')
        purse = purse + 10

    # Determine whether the roll is even or odd.
    roll_is_even = roll_total % 2 == 0

    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    player_won = bet == correct_bet

    # Display the bet results.
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # Changed the house fee from 10% to 12%.
        house_fee = int(pot * 0.12)
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # Check if the player has run out of money.
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
