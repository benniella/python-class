import random 
secret_number = random.randint(1, 10)

for attempt in range(10):
    num = int(input('Guess the secret number: '))

    if num > secret_number:
        print('\n opps! you guesssed wrong try again!')
    elif num < secret_number:
        print('\n opps! you guesssed wrong try again!')
    else:
        print('\n congratulations! you guessed the secret number!')