# Name: Robert Cuevas
# Date: October 28, 2026
# Assignment: Module 1_3
# Purpose: This program counts bottles of beer backward to 1
# and reminds the user to buy more beer.


# Function that performs the countdown
def countdown_bottles(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        bottles = bottles - 1

        if bottles == 1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.")

        print()

    # Display the final bottle using singular wording
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottles of beer on the wall.")


# Main program
print("Beer Bottles Countdown")

bottles = int(input("Enter number of bottles: "))

# Pass the user's input to the countdown function
countdown_bottles(bottles)

# Program returns here after the countdown is complete
print()
print("Time to buy more bottles of beer.")