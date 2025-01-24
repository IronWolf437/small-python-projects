# Small Translator App
This repository contains a simple yet functional translation app written in Python. The app allows users to translate text from one language to another using the `translate` library.

## Features
- Translate text from a source language to a target language.
- Intuitive console-based user interface.
- Option to return to the main menu by entering "0".
- Error handling for invalid input or connectivity issues.

## How It Works
1. The user specifies the source language (e.g., "English") and the target language (e.g., "French").
2. The user enters the text they wish to translate.
3. The app translates the text and displays the result.
4. To return to the main menu, the user can enter "0".

## Requirements
`translate` library

## Usage
Run the script:
```bash
python translator.py
```
Follow the prompts to translate text. For example:
```
welcome to small translator app
-------------------------------
[From]: Type the language you are writing in.
[To]: Type the language you want to translate to.
[Enter your text]: Enter the text you want to translate or enter "0" to return to the main menu.

from: English
to: French
enter your text: Hello, how are you?
Bonjour, comment ça va ?
```

## Example
### Input:
- Source Language: English
- Target Language: Spanish
- Text: "Good morning!"

### Output:
```plaintext
¡Buenos días!
```

## Error Handling
- If invalid input is provided or there is no internet connection, the app displays an error message:
  ```
  Input error or no internet available
  ```

## Future Improvements
Add support for GUI using a library like `Flet`.