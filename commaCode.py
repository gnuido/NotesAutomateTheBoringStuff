#commacode.py

def commaDesigner(importedList):
	if len(importedList) == 1:
		bufferList = importedList
	else:
		bufferList = ''		#bufferList is an empty string 
		for i in range(len(importedList) - 2):		#concatenates list values in a string separating them with commas
			bufferList += importedList[i] + ', '	
		bufferList += importedList[-2] + ' '			#before the last value the comma is skipped
		bufferList += 'and ' + importedList[-1]		#uses and at the end instead of a comma
	return(bufferList)
	
userDefinedList = []
while True:
	newValue = str(input('Enter a new value to add to the list, or enter nothing to end: '))
	if newValue == '':		#because every list will be displayed as a string there is a convertion of values to strings
		if len(userDefinedList) == 0:
			print('At least one value is required for the list')
			continue
		else:
			break
	else:
		try:
			userDefinedList.append(newValue)
			continue
		except ValueError:
			print('Input must be a valid data type')
			continue
#userDefinedList = ['Insfran', 'Morales', 'Cabral', 'Pintado', 'Colazo', 'Saravia', 'Castro', 'De Blasis', 'Dominguez', 'Castillo', 'Abaldo']
#2024 midseason formation of Gimnasia y Esgrima de La Plata as an example

processedList = commaDesigner(userDefinedList)
print(processedList)
