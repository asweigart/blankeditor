import logging
logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)


sumOfFibNumbers = 0


# calculate fibb sequence up to 4 million
fibNumbers = [1, 2]
while fibNumbers[-1] <= 4000000:
	fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

del fibNumbers[-1]
logging.debug(fibNumbers)

# find the even numbers
evenFibNumbers = []
for fibNumber in fibNumbers:
	if fibNumber % 2 == 0:
		evenFibNumbers.append(fibNumber)

logging.debug(evenFibNumbers)

# sum them
total = 0
for evenFibNumber in evenFibNumbers:
	total = total + evenFibNumber

print(total)