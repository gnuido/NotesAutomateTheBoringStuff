#isPhoneNumberButEvenBetter.py
#alternative pattern matching, using groups with regular expressions
import re
import pyperclip

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
text = pyperclip.paste()
mo = phoneNumberRegex.search(text)
print('Phone number found: ' + mo.group())
print('Area prefix: ' + mo.group(1))
print('Number: ' + mo.group(2))
#mo.group(0) returns the whole number

