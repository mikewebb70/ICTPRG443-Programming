# Guessing Game
from random import randrange
start = int(input("enter start number: "))
end = int(input("enter end number: "))
userNum = int(input("enter you guess, you have, : "))
ranNum = randrange(start, end)

# Main game loop
count = 0
while count < 4:
    if userNum == ranNum:
        print("you guessed the correct number", ranNum)
        break
    else:
        print("you entered the wrong number, try again", userNum)
        userNum = int(input("enter another guess: "))
        count += 1

print("Sorry you have run out of guesses")
print("the correct guess was: ", ranNum)
