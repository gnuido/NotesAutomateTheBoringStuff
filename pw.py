#! python3
#pw.py
#A passphrase manager for cavemen

passphrases = {	'userPC'	:	"wouldyoubelievethis,ariadna.theminotaurdidn'tresist",
				'email'		:	'everymanonhisown,please',
				'spotify'	:	'isthisyoujohnwayne,isthisme?'								}
																						
import sys
account = sys.argv[1]	#first command line arg is the account name

if account in passphrases:
	pyperclip.copy(passphrases[account])
	print('Passphrase for ' + account + 'copied to clipboard.')

else:
	print('No match was found.')
