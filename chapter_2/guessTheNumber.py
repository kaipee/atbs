# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20. See if you can guess.')

# Ask the player to guess 6 times
print('You have 6 attempts...')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break   # This condition is the correct guess!

if guess == secretNumber:
    print('Correct! You guessed the number in ' + str(guessesTaken) + ' tries')
else:
    print('Too many attemps! The number I was thinking of was ' + str(secretNumber) + '!')
