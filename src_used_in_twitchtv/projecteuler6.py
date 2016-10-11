
# sumOfSquares == 1*1 + 2*2 + 3*3

sumOfSquares = 0
for num in range(1, 101):
	sumOfSquares += (num * num)



# squareOfSums == (1 + 2 + 3 + 4 ...) ** 2
squareOfSums = 0
for num in range(1, 101):
	squareOfSums += num
squareOfSums = squareOfSums ** 2

#theSum = (100 * (100 + 1)) // 2
#squareOfSums = theSum ** 2

print(squareOfSums - sumOfSquares)
