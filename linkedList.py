class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None
		
	def setData(self, new_data):
		self.data = newdata
		
	def getData(self):
		return self.data
		
	def setNext(self, new_next):
		self.next = new_next
		
	def getNext(self):
		return self.next
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def isEmpty(self):
		return self.head==None
	
	#important
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count
		
	def __str__(self):
		current = self.head
		string = str(current.getData())
		while current != None:
			current = current.getNext()
			if current != None:
				string = string + "->" + str(current.getData())
		return string
		
	def reverse(self):
		previous = None
		current = self.head
		temp = self.head
		while temp!= None:
			temp = current.getNext()
			current.setNext(previous)
			previous = current
			current = temp
		self.head = previous
		
	def insert(self, item, index):
		current = self.head
		count = -1
		while current!=None and count!=index:	
			count += 1		
			if count==index:
				temp = Node(item)
				current.setNext = 
			current = current.getNext()
				
			
		
	
		
def main():
	mylist = LinkedList()
	
	mylist.add(1)
	mylist.add(2)
	mylist.add(3)
	mylist.add(4)
	print(mylist)
	
	print(f"Size of List is: {mylist.size()}")
	mylist.reverse()
	print(f"Reversing the list: {mylist}")
	
if __name__ == "__main__":
	main()