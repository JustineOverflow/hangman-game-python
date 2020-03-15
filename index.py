def game():
    guess = ['_', '_', '_', '_', '_', '_']
    solution = ['p', 'y', 't', 'h', 'o', 'n']
    i = 0
    lifes = 5

    print('Welcome! Here is the word you have to guess:')
    print(guess)

    while guess != solution and lifes > 0:
        line = raw_input("Please introduce a new letter: ")
        print(line)

        if len(line) != 1:
            print('You have to insert a single letter')

        for i, letter in enumerate(solution):
            if letter == line:
                print('you found a letter!')
                guess[i] = letter
                print(guess)

        if len(line) == 1 and line not in solution:
            lifes -= 1
            print("Wrong letter! You only have ${lifes} left!")

    if guess == solution:
        print('--> Congrats !!! You finished the game');
        print(guess)
    else:
        print("--> Sorry, you have no life left, you lost the game!")


if __name__ == '__main__':
    game()
