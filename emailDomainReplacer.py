#! python3
# - This app replaces the domain names in clipboard with provided value

import pyperclip
import re

# Regular expression to look for email address
# EMAIL_REX = re.compile(r'\w+[_\-.]?\w+@\w+\.\w+')


def email_replacer(replace_domain, work_list):
    work_list = work_list.split()
    assert len(replace_domain) > 0, 'Please enter replacement domain'
    for i in range(len(work_list)):
        work_list[i] = re.sub(r'@\w+.\w+', '@' + replace_domain, work_list[i])
    pyperclip.copy('\r\n'.join(work_list))
    print('Done!')


raw_list = pyperclip.paste()
email_replacer(input('Input the replacement domain name: '), raw_list)
