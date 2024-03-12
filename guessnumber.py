import random
# instructions: Type the range of the game, the computer will then guide you to guess the correct
# number it picked in the given range

game_range = int(input('Set the range of the game: '))


def num(x):
    # pick a random number within the given range
    computer_number = random.randint(1, x)
    # number of player's guesses
    tries = 1
    guess = 0
    while computer_number != guess:
        guess = int(input(f'pick a number between 1 and {x}: '))
        if guess == (computer_number-1) or guess == (computer_number+1):
            print('almost there')
            tries += 1
        elif guess > computer_number:
            print('Too high')
            tries += 1
        elif guess < computer_number:
            print('Too low')
            tries += 1
    print(f'You win! You have guessed the number {computer_number} correctly in {tries} guesses!')


num(game_range)
