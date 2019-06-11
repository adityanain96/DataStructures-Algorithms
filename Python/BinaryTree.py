class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.right = None
		self.left = None
		
	def setLeft(self, left_node):
		self.left = left_node
		
	def getLeft(self):
		return self.left
		
	def setRight(self, right_node):
		self.right = right_node
		
	def getRight(self):
		return self.right
		
	def setData(self, new_data):
		self.data = new_data
		
	def getData(self):
		return self.data
		
		
class Tree:
	def __init__