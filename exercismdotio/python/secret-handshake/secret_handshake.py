
def handshake(code):
	if type(code) == int:
		if code < 0:
			return []
		code = bin(code)[2:]
	else:
		try:
			int(code, 2)
		except ValueError:
			return []

	wink         = code[-1]  == '1'
	doubleBlink  = code[-2:-1] == '1'
	closeEyes    = code[-3:-2] == '1'
	jump         = code[-4:-3] == '1'
	reverseOrder = code[-5:-4] == '1'

	handshake = []
	if wink: 
		handshake.append('wink')
	if doubleBlink:
		handshake.append('double blink')
	if closeEyes:
		handshake.append('close your eyes')
	if jump:
		handshake.append('jump')
	if reverseOrder:
		handshake.reverse()

	return handshake

def code(handshake):
	# watermark constants:
	action_watermark = {'wink': 1, 'double blink': 2, 'close your eyes': 3, 'jump': 4}

	# first we check ascending order of handshake actions
	watermark = 0
	isAscending = True
	for action in handshake:
		try:
			if action_watermark[action] > watermark:
				watermark = action_watermark[action]
			elif watermark >= action_watermark[action]:
				isAscending = False
				break
		except KeyError:
			return '0'
	code = []
	if not isAscending:
		code.append('1')
	else:
		code.append('0')

	if 'jump' in handshake:
		code.append('1')
	else:
		code.append('0')

	if 'close your eyes' in handshake:
		code.append('1')
	else:
		code.append('0')

	if 'double blink' in handshake:
		code.append('1')
	else:
		code.append('0')

	if 'wink' in handshake:
		code.append('1')
	else:
		code.append('0')

	return ''.join(code).lstrip('0')
