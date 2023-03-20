def merge(x, y):
	i = 0
	p = 0
	total = []
	while i < len(x) and p <len(y):
		if x[i] <= y[p]:
			total.append(x[i])
			i += i + 1
		else:
			total.append(y[p])
			p = p +1


