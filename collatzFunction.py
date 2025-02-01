#Collatz sequence developer
def collatz(inputNumber):
	if inputNumber % 2 == 0:				#if even number
		newNumber = inputNumber // 2		#floor division
		return int(newNumber)
	else:									#odd number
		newNumber = (inputNumber * 3) + 1
		return int(newNumber)
		
number = input('Please, enter a natural number of your choosing')
while number != 1:			#Collatz sequence by definition ends in the number 1
	try:
		number = int(number)
		print(number)
		number = collatz(number)
		print(number)
		continue
	except ValueError:
		number = input('The input does not seem to be a whole number, please try again.')

print('\nThe Collatz sequence, once again, ends with the number 1!')
