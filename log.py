
def timestamp(a):
	def its_time(h, m):
		print(f"[{time.ctime()}]")
		clock = a(h, m)
		print(f"[time.ctime()}]")
		return clock
	return its_time
