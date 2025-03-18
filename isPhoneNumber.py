#isPhoneNumber.py

#script to recover phone numbers from a copied block of text, with format restriction
#needs pyperclip module to be installed

def isPhoneNumber(text):        #assuming a phone has the format 000-000-0000
    if len(text) != 12:
        return False             #checks for twelve characters
    for i in range (0,3):
        if not text[i].isdecimal():     #checks if the first three characters are, indeed, digits
            return False                #checks for correct phone number format
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False            #prone to error, interprets any string that begins with the valid format as a phone number
    return True
#-----

import pyperclip        #block of text imported from pastebin
message = pyperclip.paste()
for i in range(len(message)):       
    chunk = message[i:i+12]             
    if isPhoneNumber(chunk):            #takes each chunk of text and verifies it
        print('Phone number found: ' + chunk)
print('Done')
