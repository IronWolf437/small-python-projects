# Number Guessing Game 🎯
A simple Python game where players try to guess a random number between 1 and 100. The player has **7 attempts** to guess the correct number. If they don't guess correctly, the game reveals the target number.

## How to Play:
1. Run the program.
2. Enter `[s]` to start the game or `[q]` to quit.
3. Guess a number between 1 and 100.
4. The program provides feedback after each guess:
   - **"Too low"** if the guess is smaller than the target.
   - **"Too high"** if the guess is larger than the target.
   - **"You are close"** if the guess is within 10 of the target.
   - **"You win"** if the guess matches the target.

## Features:
- User-friendly interface with colored messages for better feedback.
- Option to play multiple rounds without restarting the program.
- Validates input to avoid crashes.