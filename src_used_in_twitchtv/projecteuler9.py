import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

# a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2

'''
# this is too slow. So many of the a,b,c combinations don't add up to 1000
for a in range(1, 1001):
  for b in range(1, 1001):
    for c in range(1, 1001):
      if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)
'''


# imagine a number line: 1 2 3 4 5 ... 1000
# now imagine 2 lines dividing this number line into segments:
# 1 2 | 3 4 5 | 6 7 ... 1000
# In the above example, segment1 = 2 and segment2 = 5.
# We can calculate a as 2, b as 3, and c as 995.
# No matter what the segmentation is with segment1 and segment2, a,b, & c ALWAYS add up to 1000
# This saves us from checking many needless combinations.
segment1 = 1
segment2 = 1
while True:
  a = segment1
  b = segment2 - segment1
  c = 1000 - segment2

  logging.debug('%s, %s | %s, %s, %s, %s' % (segment1, segment2, a, b, c, a+b+c))
  
  if a ** 2 + b ** 2 == c ** 2:
    print(a * b * c)	
    break

  segment2 += 1
  if segment2 == 1000:
  	segment1 += 1
  	segment2 = segment1

  	if segment1 == 999:
  		print('couldnt find any answer')
  		break
