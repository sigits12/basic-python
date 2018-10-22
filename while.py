number = 20
running = True

while running:
    guess = int(input('Enter a number: '))

    if guess == number:
        print('Yay, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that. ')
    else:
        print('No, it is a little lower than that.')

else:
    print('The while loop is over.')

print('Done')
