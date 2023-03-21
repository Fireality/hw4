def palindrome(a):
	n = len(a)
	for i in range (n // 2):
		if a[i] != a[n- i -1]:
			return False
	return True
#Test1
