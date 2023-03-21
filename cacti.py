def cacti_number(plant):
	rows = len(plant)
	column = len(plant[0])
	count = 0

	for i in range(rows):
		for p in range (column):
			if plant[i][p] == 0:
				diagonal = True
				if i > 0 and plant[i-1][p] == 1:
					diagonal = False
				if p > 0 and plant[i][p-1] == 1:
					diagonal = False
				if i < rows -1 and plant[i+1][p] == 1:
					diagonal = False
				if p < column -1 and plant[i][p+1] == 1:
					diagonal = False
				if i > 0 and p > 0 and plant[i-1][p-1] == 1:
					diagonal = False
				if i > 0 and p < column - 1 and plant [i-1][p+1] == 1:
					diagonal = False
				if i < rows -1 and p > 0 and plant[i+1][p-1] == 1:
					diagonal = False
				if i < rows -1 and p < column -1 and plant[i+1][p+1] == 1:
					diagonal = False
				if diagonal:
					count = count + 1
	return count
