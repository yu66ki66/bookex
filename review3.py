def devide10(x):
	"""
	returns x / 10.
	:param x: float.
	:return: float num devided by 10.
	"""
	return x / 10

try:
	numstr = input("type a number:")
	num = float(numstr)
	result = devide10(num)
	print(result)
except(ZeroDivisionError,ValueError):
	print("Invalid Input")