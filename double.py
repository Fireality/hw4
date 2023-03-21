def double (a):
	def rewind_time():
		a()
		print("Let's try that again!")
		a()
	return rewind_time
