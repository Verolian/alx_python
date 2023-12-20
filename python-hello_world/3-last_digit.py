import random
# Generate a random number between -10000 and 10000
number = random.randint(-10000 and 10000)
# Extract the last digit, preserving sign
if number >= 0:
    rem = number % 10
else:
    rem = number % -10
# Print the output based on the last digit
    print("Last digit of", number, "is", rem, end=" ")
    if rem > 5:
        print("and is greater than 5")
    elif rem == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")