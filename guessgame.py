import random
import calendar

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


# print(calendar.firstweekday())
# print(calendar.weekheader(5))
# print(calendar.month(2020, 4))
# print(calendar.weekday(2020, 4, 22))

def reminder(the_year, the_month, the_day, name):
    day = calendar.weekday(the_year, the_month, the_day)
    if day == 0:
        print('Monday')
    elif day == 1:
        print('Tuesday')
    elif day == 2:
        print('Wednesday')
    elif day == 3:
        print('Thursday')
    elif day == 4:
        print('Friday')
    elif day == 5:
        print('Saturday')
    elif day == 6:
        print('Sunday')
    print(f'Today is {name} birthday ')


# day = {'year': 4, 'month': int(), 'day': int()}
# print(day['year'])

def prompt_input():
    enter_year = input('Enter year: ')
    enter_month = input('Enter month i.e 1-12: ')
    enter_day = input('Enter day i.e 1-31: ')

    Day = int(enter_day)
    Month = int(enter_month)
    Year = int(enter_year)

    day = calendar.weekday(Year, Month, Day)

    if day == 0:
        print('Monday')
    elif day == 1:
        print('Tuesday')
    elif day == 2:
        print('Wednesday')
    elif day == 3:
        print('Thursday')
    elif day == 4:
        print('Friday')
    elif day == 5:
        print('Saturday')
    elif day == 6:
        print('Sunday')


prompt_input()