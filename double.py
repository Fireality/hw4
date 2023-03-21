def double (top_of_the_morning):
	def rewind_time():
		top_of_the_morning()
		print("Let's try that again!")
		top_of_the_morning()
	return rewind_time
