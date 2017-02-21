def greatest_common(a,b):
	"""Method that finds greatest common denominator.
	Input is 2 numbers. Output of this method is greatest common denominator."""
	print a, b
	if a == b:
		return a
	else:
		for x in range (1, min(a,b) + 1):
			# print x
			if a % x == 0  and  b % x == 0:
				greatest_common_divider = x
	return greatest_common_divider



print greatest_common(120,20)