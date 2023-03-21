import time

def timestamp(a):
	def its_time(*args, **kwargs):
		print(time.ctime())
		return a(*args, **kwargs)
	return its_time
