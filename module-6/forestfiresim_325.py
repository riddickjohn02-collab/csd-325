"""CSD-325 Module 6 - Forest Fire Simulation with a Lake.

Student: Robert Cuevas
Team members: [add remaining team members]
Date: November 18, 2026

Based on the provided forestfiresim.py, modified by Sue Sampson from a
program by Al Sweigart.

Changes for Module 6:
1. Added a central lake made of blue W characters.
2. Kept the lake permanent when creating each new simulation frame.
3. Protected water from tree growth, lightning, and spreading fire.
4. Preserved the existing forest growth, fire behavior, and Ctrl-C exit.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires bext. Install it with: python -m pip install bext')
    sys.exit(1)

# Original simulation constants.
WIDTH = 79
HEIGHT = 22
TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'  # NEW: A distinct character for the lake.

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

# NEW: Define a rectangular lake near the middle of the forest.
# A coordinate is lake water if it falls within these boundaries.
LAKE_WIDTH = 9
LAKE_HEIGHT = 12
LAKE_LEFT = (WIDTH - LAKE_WIDTH) // 2
LAKE_TOP = (HEIGHT - LAKE_HEIGHT) // 2


def isLake(x, y):
    """Return True if this cell belongs to the permanent central lake."""
    return (LAKE_LEFT <= x < LAKE_LEFT + LAKE_WIDTH
            and LAKE_TOP <= y < LAKE_TOP + LAKE_HEIGHT)


def createNewForest():
    """Create the original forest with a blue-water lake in the center."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isLake(x, y):  # NEW: Water takes priority over trees.
                forest[(x, y)] = WATER
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def updateForest(forest):
    """Compute one simulation step without ever changing water cells."""
    nextForest = {'width': forest['width'], 'height': forest['height']}

    for x in range(forest['width']):
        for y in range(forest['height']):
            # NEW: Preserve water on every step, even if nearby cells burn.
            if forest[(x, y)] == WATER:
                nextForest[(x, y)] = WATER
                continue

            # Original behavior: cells already reached by spreading fire
            # should not be overwritten later in this same simulation step.
            if (x, y) in nextForest:
                continue

            if (forest[(x, y)] == EMPTY
                    and random.random() <= GROW_CHANCE):
                nextForest[(x, y)] = TREE
            elif (forest[(x, y)] == TREE
                  and random.random() <= FIRE_CHANCE):
                nextForest[(x, y)] = FIRE
            elif forest[(x, y)] == FIRE:
                for ix in range(-1, 2):
                    for iy in range(-1, 2):
                        neighbor = (x + ix, y + iy)
                        # NEW: Fire spreads only into trees, never water.
                        if (forest.get(neighbor) == TREE
                                and not isLake(*neighbor)):
                            nextForest[neighbor] = FIRE
                nextForest[(x, y)] = EMPTY
            else:
                nextForest[(x, y)] = forest[(x, y)]

    return nextForest


def displayForest(forest):
    """Display trees in green, fire in red, and lake water in blue."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
            elif cell == FIRE:
                bext.fg('red')
            elif cell == WATER:  # NEW: Display water in blue.
                bext.fg('blue')
            else:
                bext.fg('reset')
            print(cell, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)
        forest = updateForest(forest)
        time.sleep(PAUSE_LENGTH)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.fg('reset')
        print('\nForest fire simulation ended.')
        sys.exit(0)
