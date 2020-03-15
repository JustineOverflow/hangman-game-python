def check(a, b):
    if a == b:
        return True
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False

    for i in a:
        if i == i in b:
            return False

    return True

def game():
    guess = ['_', '_', '_', '_', '_', '_']
    solution = ['p', 'y', 't', 'h', 'o', 'n']
    i = 0
    lifes = 5

    print('Welcome! Here is the word you have to guess:')
    print(guess)

    while not check(guess, solution) and lifes > 0 :
        line = "Please introduce a new letter: "
        print(line)

        if len(line) != 1:
            print('You have to insert a single letter')

        for i in solution:
            if i == i in line:
                print('you found a letter!')
                i in guess == i in solution
                print(guess)

        if len(line) == 1 and not solution.includes(line):
            lifes -= 1
            print("Wrong letter! You only have ${lifes} left!")

    if check(guess, solution):
        print('--> Congrats !!! You finished the game');
        return guess
    else:
        print("--> Sorry, you have no life left, you lost the game!")

game()
