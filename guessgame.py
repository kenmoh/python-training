import random

# Guessing Game

def guessGame():
    first_secrete = 'Aremoh'  #What to guess
    second_secrete = 'Kenneth'
    first_guess = ''
    second_guess = ''
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    total_guess = []

    while first_guess != first_secrete.lower() and second_guess != second_secrete and not out_of_guesses:
        if guess_count < guess_limit:
            first_guess = input('Enter first guess: ')
            second_guess = input('Enter second guess: ')
            total_guess.append(first_guess)
            total_guess.append(second_guess)
            guess_count += 1

        else:
            out_of_guesses = True

    if out_of_guesses:
        print('Out of guesses, YOU LOSE ! Ans: ', first_secrete, second_secrete)
    else:
        print('You Win, GOOD JOB !')
        print(total_guess)



# A Guessing game to guess between 1 to 6
def guessNumber():
    random_num = random.randint(1, 6)
    guess = int()
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != random_num and not out_of_guesses:
        if guess_count < guess_limit:
            guess = int(input('Enter a number between 1 and 6: '))
            if guess > 6:
                print('Your guess is out of range !')
                guess = int(input('Enter a number between 1 and 6: '))
            elif guess < 1:
                print('Your guess is below range!')
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print('Your guesses are wrong, PLAY AGAIN!')

    else:
        print('You guessed correctly, WELDONE !')


guessNumber()
