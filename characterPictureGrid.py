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
for x in range(len(grid) - axisDifference):		#9
	print(end='\n')
	for y in range(len(grid[x]) + axisDifference):		#6
		print(grid[y][x], end='')
