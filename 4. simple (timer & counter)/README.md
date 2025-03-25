# TimeCount
TimeCount is a simple Python-based console application that functions as both a **Timer** and a **Stopwatch**. It provides a minimalistic yet functional approach to time tracking directly from the terminal.

## Features
- **Timer Mode**: Counts down from a user-specified time (in minutes).
- **Stopwatch Mode**: Tracks elapsed time in hours, minutes, and seconds.
- **Help Menu**: Provides instructions on how to use the program.
- **User-Friendly Interface**: Uses color-coded output for better readability.
- **Error Handling**: Prevents incorrect input by validating user entries.

## How It Works
1. **Start the Program**: Run the Python script in a terminal.
2. **Choose an Operation**:
   - Enter **'t'** to start the Timer.
   - Enter **'s'** to start the Stopwatch.
   - Enter **'h'** to view the help menu.
3. **For Timer Mode**:
   - Enter the number of minutes to count down.
   - The program will display the remaining time until it reaches zero.
4. **For Stopwatch Mode**:
   - The stopwatch will start at `00:00:00` and increment until manually stopped.
   - The maximum time limit is **24 hours**.
5. **Error Handling**:
   - Entering an invalid value (e.g., letters instead of numbers) will result in an error message.

## Dependencies
- **Python 3.x**
- **time module** (built-in)

## Possible Improvements
- **GUI Version**: Implementing a graphical interface using Tkinter or PyQt.
- **Pause & Resume**: Adding functionality to pause and resume both the timer and stopwatch.
- **Audio Alerts**: Playing a sound when the timer reaches zero.
- **Command-Line Arguments**: Allowing users to start the timer/stopwatch with predefined values.

## How to Run
```sh
python timer.py
```

---
Feel free to contribute to this project by suggesting improvements or adding new features!

