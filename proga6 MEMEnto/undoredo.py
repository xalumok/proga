from copy import deepcopy

max_cnt = 5

class Mem:
	def __init__(self, originator):
		self.originator = originator
		self.mementos = list()
		self.index = 0

	def save(self):
		while self.index + 1 < len(self.mementos):
			self.mementos.pop()
		if self.index == max_cnt - 1:
			self.mementos.pop(0)
		self.mementos.append(deepcopy(self.originator))
		self.index = len(self.mementos) - 1

	def undo(self):
		if self.index > 0:
			self.index -= 1
			self.originator.__dict__ = self.mementos[self.index].__dict__.copy()

	def redo(self):
		if self.index + 1 < len(self.mementos):
			self.index += 1
			self.originator.__dict__ = self.mementos[self.index].__dict__.copy()