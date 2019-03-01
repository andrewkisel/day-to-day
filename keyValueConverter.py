#! python3
# This app is a simple abbreviation to full name converter

import sys
import pyperclip
from zipCodeDB import CC_MAPPING, LE_MAPPING, STATE_MAPPING, BUS_FIELD_MAPPING


def abbrev_converter(codes, mapping):
    if '\n' in codes:
        line = codes.split('\n')  # Make a list of strings.
        for i in range(len(line)):  # Loop through all the items in the list, make necessary changes.
            line[i] = mapping.get(line[i].upper().rstrip('\r'), 'No such value: ' + line[i])
        res = '\n'.join(line)  # Convert to string, separator '\n'
    elif ',' in codes:
        line = codes.split(',')  # Make a list of strings. Separator - ','
        for i in range(len(line)):  # Loop through all the items in the list, make necessary changes.
            line[i] = mapping.get(line[i].upper().rstrip('\r'),
                                  'No such value: ' + line[i])
        res = ', '.join(line)  # Convert to string, separator ', '
    elif '\n' and ',' not in codes:
        res = mapping.get(codes.upper().rstrip('\r'), 'No such value: ' + codes)
    else:
        print('Please check your input!')
        sys.exit()
    print('Converted successfully!' + '\n'
          + 'Results are in your clipboard.')
    return res


def option(in_type):
    # Identify the input type and call converter appropriately
    if in_type == 1:
        return pyperclip.copy(abbrev_converter(raw_data, CC_MAPPING).title())
    elif in_type == 2:
        return pyperclip.copy(abbrev_converter(raw_data, LE_MAPPING))
    elif in_type == 3:
        return pyperclip.copy(abbrev_converter(raw_data, STATE_MAPPING).title())
    elif in_type == 4:
        swap_cc_mapping = {v: k for k, v in CC_MAPPING.items()}
        return pyperclip.copy(abbrev_converter(raw_data, swap_cc_mapping))
    elif in_type == 5:
        swap_state_mapping = {v: k for k, v in STATE_MAPPING.items()}
        return pyperclip.copy(abbrev_converter(raw_data, swap_state_mapping))
    elif input_type == 6:
        return pyperclip.copy(abbrev_converter(raw_data, BUS_FIELD_MAPPING).title())
    else:
        return print('Please choose values from 1 to 5 only!')


input('DISCLAIMER: App only supports comma or newline delimited values' + '\n'
      + 'please copy input into your clipboard and press any key...' + '\n')
input_type = int(input('What type of data do you need to convert?' + '\n' + '\n'
                       + 'Press 1 for country code to full name' + '\n'
                       + 'Press 2 for country code to legal entity' + '\n'
                       + 'Press 3 for state abbreviation to full name' + '\n'
                       + 'Press 4 for full country name to abbreviation' + '\n'
                       + 'Press 5 for full state name to abbreviation' + '\n'
                       + 'Press 6 for NLSU research area to Salesforce business field' + '\n'))
raw_data = pyperclip.paste().rstrip('''!"#$%&'(*+-./:;<=>?@[\]^_`{|}~\n''')
option(input_type)
