class BufferEmptyException(Exception):
	pass

class BufferFullException(Exception):
	pass

class CircularBuffer():
	def __init__(self, bufferSize):
		self.buffer = [None] * bufferSize
		self.start = 0
		self.end = 0
		self.size = 0

	def read(self):
		# check if buffer is empty
		if self.size == 0:
			raise BufferEmptyException()

		# pop value from start
		result = self.buffer[self.start]
		self.size -= 1

		# increment start pointer
		self.start += 1
		if self.start == len(self.buffer):
			self.start = 0

		return result

	def write(self, value):
		# check if buffer is full
		if self.size == len(self.buffer):
			raise BufferFullException()

		self.size += 1
		
		# push value
		self.buffer[self.end] = value

		# increment end pointer
		self.end += 1
		if self.end == len(self.buffer):
			self.end = 0

		
	def overwrite(self, value):
		# check if buffer is full
		if self.size == len(self.buffer):
			self.read()
		self.write(value)

	def clear(self):
		self.start = 0
		self.end = 0
		self.size = 0