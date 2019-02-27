#! python3
# Takes all the data from clipboard and changes it's case

import pyperclip
import sys


def magic(output_type, data):
    if output_type == 1:
        pyperclip.copy(data.upper())
    elif output_type == 2:
        pyperclip.copy(data.lower())
    elif output_type == 3:
        pyperclip.copy(data.title())
    else:
        print('Please choose values from 1 to 3')
        sys.exit()
    return print('Done and copied to clipboard!')


print('DISCLAIMER: This app allows you to change the case of text without changing its formatting')
mod_type = int(input('Please copy values that you would like to uppercase' + '\n'
                     + 'Press 1 to uppercase, 2 to lowercase, 3 to title case: ' + '\n'))
insert = pyperclip.paste()
magic(mod_type, insert)
