#fantasyGameInventory.py

aidQuantity =	{'Stimpak' : 4,		#example taken from Fallout: New Vegas
				"Doctor's bag" : 1,	#carrying only aid items in invetory
				'Rad-x' : 4,
				'Radaway' : 4,
				'Med-x' : 6,
				'Buffout' : 1,
				'Psycho' : 3,
				'Purified water' : 4,
				'Sunset sarsaparilla' : 8,
				"Patriot's cookbook" : 1,
				'¡La Fantoma!' : 2,
				'Big book of science' : 1}

aidWeight =	{'Stimpak' : 1,
			"Doctor's bag" : 2,
			'Rad-x' : 0,
			'RadAway' : 0,
			'Med-x' : 0,
			'Buffout' : 0,
			'Psycho' : 0,
			'Purified water' : 1,
			'Sunset sarsaparilla' : 0,
			"Patriot's cookbook" : 0,
			'¡La Fantoma!' : 0,
			'Big book of science' : 2}
		
def aidTab(aidQuantity, aidWeight):
	print('#---------------------------#')
	totalWeight = 0
	
	for weights in aidWeight.values():
		totalWeight += weights
	totalWeight = str(totalWeight)
	
	print('< Aid >', '\tWeight[' + f'{totalWeight}' + '/250]')
	
	for k,v in aidQuantity.items():
		print(k + '(' + str(v) + ')')
	
	print('#---------------------------#')
	print('O'.rjust(5, ) + 'O'.rjust(10, ) + 'O'.rjust(10, ) + '\n' + 'STATUS'.rjust(7, ) + 'ITEMS'.rjust(10, ) + 'DATA'.rjust(10, ))
	#homemade pipboy interface 
	
aidTab(aidQuantity, aidWeight)
		
