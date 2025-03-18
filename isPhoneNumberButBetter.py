#isPhoneNumberButBetter.py

#a script to recover phone numbers from a block of text, using regular expressions.Less prone to error, it matches format strictly.

import re
import pyperclip        #requires pyperclip module to be installed

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')     #RegEx = REGular EXpression | r prevents having to use \\ because of escape characters, it indicates that the following is a raw string
text = pyperclip.paste()
mo = phoneNumberRegex.search(text)      #mo = match object
print('Phone number found: ' + mo.group())      #mo.group prints all matches

