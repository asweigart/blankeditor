def on_square(squareNumber):
	return 2 ** (squareNumber - 1)
	
	"""
	grains = 1
	for i in range(2, squareNumber + 1):
		grains *= 2
	return grains
	"""

def total_after(squareNumber):
	return (2 ** squareNumber) - 1
	
	"""
	total = 0
	for i in range(1, squareNumber + 1):
		total += on_square(i)
	return total
	"""