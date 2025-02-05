grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

axisDifference = len(grid) - len(grid[0])	#this will only work for this given grid an equally lenghted lists of lists
for x in range(len(grid) - axisDifference):	
	print(end='\n')		#starts a new line
	for y in range(len(grid[x]) + axisDifference):	#lenght of one of the list contained in the grid list
		print(grid[y][x], end=' ')		#inverted order of coordinates to transpose values
										#no input after each print but a space for better output
