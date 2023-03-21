def cacti_count(plant):
	rows = len(plant)
	column = len(plant[0])
	count = 0

	for i in range(rows):
		for p in range (column):
			if plant[i][p] == 0:
				diagonal = False
				if i > 0 and plant[i-1][p] == 1:
					diagonal = True
				if p > 0 and plant[i][p-1] == 1:
					diagonal = True
				if i < rows -1 and plant[i+1][p] == 1:
					diagonal = True
				if p < column -1 and plant[i][p+1] == 1:
					diagonal = True
				if i > 0 and p > 0 and plant[i-1][p-1] == 1:
					diagonal = True
				if i > 0 and p < column - 1 and plant [i-1][p+1] == 1:
					diagonal = True
				if i < rows -1 and p > 0 and plant[i+1][p-1] == 1:
					diagonal = True
				if i < rows -1 and p < column -1 and plant[i+1][p+1] == 1:
					diagonal = True

				if not diagonal:
					count += 1
	return count

def cacti_number(a)
	def wrapper(*args, **kwargs):
	plant = args[0]
	rows = len(plant)
	column = len(plant[0])
	max_cacti = 0
	for i in range(rows):
		for p in range (column):
			if plant[i][p] == 0:
				diagonal = False
				if i > 0 and plant[i-1][p] == 1:
					diagonal = True
				if i < rows-1 and plant[i+1][p] == 1:
					diagonal = True
				if p > 0 and plant[i][p-1] == 1:
					diagonal == True
				if p < column -1 and plant[i][p+1] == 1:
					diagonal = True
				if i > 0 and p > 0 and plot[i-1][p-1] == 1:
					diagonal = True
				if i > 0 and p < column -1 and plant[i-1][p+1] == 1:
					diagonal = True
				if i < rows -1 and p > 0 and plant[i+1][p-1] == 1:
					diagonal = True
				if i < rows -1 and p <column -1 and plot[i+1][p+1] == 1:
					diagonal = True
				if not diagonal:
					test_plant = [row[:] for row in plant]
				test_plant[i][p] = 1
			cacti_count = count_cacti(test_plant)
			if cacti_count > max_cacti:
				max_cacti = cacti_count
	return a(*args, **kwargs), max_cacti
	return wrapper
