import time

min = 0
hr = 0
state = True

print("-------------------(TimeCount_v1.1)-------------------")        # This line displays the name and versions of the program

print("\033[0;35mCan enter 'h' in [type of operations] To help you understand the program....\033[0m") # This is an explanatory line for the user to enter "help" to understand the program

while True:
    dif = input("Enter the type of operations: ")

    if dif == "h":
         print('''\033[0;32m

Welcome to the 'help' menu. This menu will help facilitate dealing with the program:

               
type of operations              definition
h                               help you understand the program
t                               It's Timer App
S                               İt's StopWatch App

# Important notes:
 ----------------------------------------------------------------------
| -> When asked to enter a 'number', do not enter a 'phrase'.          |
|     ex:                                                              |
|     - Enter number of minutes: 4      >>  This entry is correct      |
|     - Enter number of minutes: hbu    >>  This entry is incorrect    |
 ----------------------------------------------------------------------

\033[0m''')

    try:
        if dif == "t":
            print("\033[0;33m1. Timer app:\033[0m")
            min_input = int(input("\033[0;33mEnter number of minutes: \033[0m"))

            for i in range(min_input,-1,-1):
                if i == i:
                    i-= 1
                for sec in range(59, -1,-1):
                    print(f"\033[0;33m[{i:02}:{sec:02}]\033[0m", end='', flush=True)
                    time.sleep(1)
                    print('\r', end='')

                if sec == 0 and i == 0:
                    break
            print("\033[0;36mTime is over....\033[0m"+ '\n')
        
        elif dif == "s":
            print("\033[0;33m2. Stop Watch app:\033[0m")
            while state:
                for sec in range (60):
                    print(f"\033[0;33m[{hr:02}:{min:02}:{sec:02}]\033[0m", end='', flush=True)
                    time.sleep(1)
                    print('\r', end='')

                    if sec == 59:
                        min += 1
                        if min == 59:
                            min = 0
                            hr += 1
                            if hr == 24:
                                hr = 0
                                state = False
                                print('\n' + "\033[0;36mThe maximum number of '24 hours' has been reached....\033[0m"+ '\n')

    except ValueError:          # Prints an error message if the user enters a phrase instead of a number in the number'entry unit
        print('\n' + "\033[0;31mConfiguration error. You must enter a'number' not a 'phrase'\033[0m" + '\n')