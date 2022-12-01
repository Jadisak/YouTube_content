import random

while True:
    print('Welcome to the game\n You have to guess the correct number between 2 numbers. Best of luck !!')
    from_num = int(input('Enter the first number:'))
    to_num = int(input('Enter the second number:'))
    guess = random.randint(from_num, to_num)
    def main_function():
        global from_num, to_num, guess
        answer = int(input('Guess the number:'))
        if answer == guess:
            print('You guess it correctly !!')
        else:
            print('Sorry , try again !!')
            main_function()
    main_function()