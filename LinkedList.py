class Node:
    """
    This is a class of the basic building block of linked list - Node
    The Node class also includes the usual methods to access and modify the 
    data and the next reference.    
              
    Attributes
    ----------
        data : 
            This where we store the list item
        next : 
            Holds the reference to the next Node (default is None)
    
    
    """
    def __init__(self,initdata):
        """
        Parameters
        ----------
        initdata :
            Initial data value for the Node
        """
        self.data = initdata
        self.next = None
    
        
    def getData(self):
        """        
        Returns
        -------
            data
                item stored in current Node
                
        """
        return self.data
    
    def getNext(self):
        """
        Returns
        -------
            next
                reference to the next Node
        """
        return self.next
    
    def setData(self,newdata):
        """
        Parameters
        ----------
        newdata : 
            this is new data to be stored in the Node
        Attributes
        ----------
        data : 
            this where new data item is stored
        """
        self.data = newdata
        
    def setNext(self,newnext):
        """
        Parameters
        ----------
        newnext : 
            this is the next node
        Attributes
        ----------
        next : 
            Holds the reference to the next Node
        """
        self.next = newnext
        
    
class unorderedList:
    """
    This is class of unordered list.
    Attributes
    ----------
    head : 
        Each unorderedList object will maintain a single reference to the head
        object        
    """
    def __init__(self):
        """
        Attributes
        ----------
        head : 
            head holds reference to the start of the list (default is None)
        """
        self.head = None
        
    def isEmpty(self):
        """
        Returns
        -------
        isEmpty : bool
        """
        return self.head == None
    
    def add(self,item):
        """Adds new item to the list
        Parameters
        ----------
        item : 
            this is the data value that will be added to the list
        Attributes
        ----------
        temp : Node
            stores the newely created Node
            
        """
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
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found    