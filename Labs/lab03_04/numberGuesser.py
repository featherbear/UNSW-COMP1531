'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    return [n for n in values if n is not guess]

def find_closest(guess, values):
    # This function should return the value that is closest to `guess`
    return sorted(values, key = lambda n: abs(n - guess))[0]

def run_game(values):
    # While there are values to be guessed and the user hasn't quit (with 'q'), 
    # the game should wait for the user to input their guess and then 
    # reveal whether the closest number is lower or higher.

    print(f'Numbers are between {MIN} and {MAX} inclusive.')
    
    guess = None
    
    while guess is None:
        print('There are {len(values)} values left.', end=" ")
        guess = input('Guess: ')

        if guess == "q": break
        guess = int(guess)
        
        if guess in values:
            print(f'You found {guess}! It was in the list')
            values = handle_guess(guess, values)
        else:
            print(f'The closest to {guess} is {find_closest(guess, values)}')
      
        if len(values) == 0:
            print("Congratulations! You won!")
            break
            
    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    # Generate a random list and run the game
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)