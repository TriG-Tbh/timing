def __init__():
	global time
	import time
	global traceback
	import traceback
	global itemgetter
	from operator import itemgetter
	global starttime, stoptime, times
	times = {}
	starttime = 0
	stoptime = 0

def start(name):
	if not isinstance(name, str):
		raise TypeError(f"invalid type for name \"{name}\": {type(name)}")
	starttime = time.time()
	times[name] = starttime

def stop(name):
	if not isinstance(name, str):
		raise TypeError(f"invalid type for name \"{name}\": {type(name)}")
	if name not in times:
		raise ValueError(f"name \"{name}\" not found in times")
	stoptime = time.time()
	times[name] = stoptime - times[name]

def execute(name, code):
	if not isinstance(name, str):
		raise TypeError(f"invalid type for name \"{name}\": {type(name)}")
	if not isinstance(code, str):
		raise TypeError(f"invalid type for code \"{name}\": {type(name)}")
	start(name)
	try:
		exec(code)
	except Exception as e:
		raise e
	stop(name)


def display(values, descending=False):
	sortedtimes = {}
	if not isinstance(descending, bool):
		raise TypeError(f"invalid type for descending: {type(values)}")
	if not isinstance(values, list):
		raise TypeError(f"invalid type for values: {type(values)}")
	for name in values:
		if name not in times:
			raise ValueError(f"name \"{name}\" not found in times")
		sortedtimes[name] = times[name]
	sortedtimes = sorted(sortedtimes.items(), key=itemgetter(1), reverse = descending)

	for counter, pos in enumerate(sortedtimes, 1):
		color = ""
		if counter == 1:
			color = "\u001b[32;1m"
		elif counter == (len(sortedtimes) // 2) + 1 and (len(sortedtimes) % 2) != 0:
			color = "\u001b[33;1m"
		elif counter == len(sortedtimes):
			color = "\u001b[31;1m"
		
		print(color + str(counter) + ": " + pos[0] + " (" + str(pos[1]) + ")" + "\u001b[0m")

def timefunction(func):
	def wrapper():
		start(func.__name__)
		func()
		stop(func.__name__)
	wrapper()
	return wrapper

def sumtimes(values):
	if not isinstance(descending, bool):
		raise TypeError(f"invalid type for descending: {type(values)}")

	total = 0

	for counter, pos in enumerate(sortedtimes, 1):
		color = ""
		if counter == 1:
			color = "\u001b[32;1m"
		elif counter == (len(sortedtimes) // 2) + 1 and (len(sortedtimes) % 2) != 0:
			color = "\u001b[33;1m"
		elif counter == len(sortedtimes):
			color = "\u001b[31;1m"
		
		print(color + str(counter) + ": " + pos[0] + " (" + str(pos[1]) + ")" + "\u001b[0m")

		total += pos[1]

	print("\u001b[32;1m" + "Total time: " + str(total) + "\u001b[0m")	
	

if __name__ == "__main__":
	pass
else:
	__init__()
