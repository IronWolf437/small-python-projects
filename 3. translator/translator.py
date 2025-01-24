from translate import Translator

print('welcome to small translator app')
print('-------------------------------')
print('''[From]: Type the language you are writing in.
[To]: Type the language you want to translate to.
[Enter your text]: Enter the text you want to translate or enter "0" to return to the main menu.''')

# Create a translator object
# You can specify the source language (from_lang) and the target language (to_lang)
while True:
    try:
        translator = Translator(from_lang=input('\n\033[0;32mfrom: \033[0m'), to_lang=input('\033[0;32mto: \033[0m'))

        while True:
            entry = input('\033[0;36menter your text: \033[0m')
            # Translate the text
            translation = translator.translate(entry)
            
            if entry == '0':
                break
            
            # Print the translated text
            print(translation)

    except:
        print('\033[4;31mInput error or no internet available\033[0m')