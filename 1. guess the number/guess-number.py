from random import*

# welcome message:
print('welcome to the number guessing game')
print('-----------------------------------')
print('you have 7 chances to guess the number for win the game...\n')

# Generate a random number between 1 and 100:
target = randint(1,101)

while True:
    # Ask the user for their guess:
    state = input('\033[1;34menter state fo game [s] to start or [q] to quit: \033[0m')

    if state == 's':
        for i in range(7):
            try:
                # Ask the user for a number between 1 and 100
                UserInput = int(input('\033[0;36menter any number from 1 to 100: \033[0m'))
                # If the user's guess is equal to the target number:
                if UserInput == target:
                    print('\033[0;32myou win...\033[0m\n')
                    break
                # If the user's guess is within 10 of the target number:
                elif abs(UserInput - target) <= 10:
                    print('\033[0;35myou are close\033[0m')
                # If the user's guess is lower than the target number:
                elif UserInput < target:
                    print('\033[0;35mtoo low\033[0m')
                # If the user's guess is higher than the target number:
                elif UserInput > target:
                    print('\033[0;35mtoo high\033[0m')
                
            except ValueError:
                print('\033[0;31mplease enter a number\033[0m')

        # If the user has used up all 7 guesses without guessing the target number:
        else:
            print('\n\033[0;33mtime is over you are loss...\033[0m')
            print(f'\033[0;33mcorrect number is : {target}\033[0m\n')
    
    elif state == 'q':
        break