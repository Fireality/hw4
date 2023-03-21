def merge(x, y):
	i = 0
	p = 0
	combine = []
	while i < len(x) and p < len(y):
		if x[i] <= y[p]:
			combine.append(x[i])
			i = i + 1
		else:
			combine.append(y[p])
			p = p + 1
	combine.extend(x[i:])
	combine.extend(y[p:])
	return combine


