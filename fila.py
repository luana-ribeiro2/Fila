class Fila:
	def __init__(self,size):
		self.__items = []
		self.__maxSize = size

	def __repr__(self):
		return repr(self.__items)

	def __str__(self):
		return str(self.__items)

	def __len__(self):
		return len(self.__items)

	def maxSize(self):
		return self.__maxSize

	def enqueue(self, item):
		self.__items.append(item)

		if len(self.__items) > self.__maxSize:
			raise RuntimeError('estouro da fila!') 

	def dequeue(self):
		item = self.__items[0]
		del self.__items[0]
		return item

x = Fila(6)
x.enqueue(1)
x.enqueue(1)
x.enqueue(1)
x.enqueue(1)
x.enqueue(1)
x.enqueue(1)
x.dequeue()
x.enqueue(1)
x.enqueue(1)
print(x)

