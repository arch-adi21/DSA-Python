# Using a class we can create the Node of the LinkedList

class Node :
  
  # We will initiate this Node by defining the element and the pointer through __init__ constructor

  def __init__(self , element = None , nxtPointer = None) :
    
    self.element = element
    self.nxtPointer = nxtPointer

# Create a new class LinkedList , which will use Nodes to store data .

class LinkedList:

    # Initiate the head of the LinkedList
    def __init__(self):
        self.head = None

    #This method will help you to add an element at the head position of the linked list
    def add_from_front(self, element):
        node = Node(element , self.head) # assign a Node to a variable and use the previous head as the pointer
        self.head = node # update the assigned node as the new head. 
    
    #THis method will help you to add an element at the end of the linked list
    def add_from_end(self, element):
        if self.head == None :
            self.head = Node(element , None) # If the linked list is empty , then add the element as the head
            return
        itr = self.head
        while itr.nxtPointer :
            itr = itr.nxtPointer # Traverse the linked list till the end
        itr.nxtPointer = Node(element , None) # Add the element at the end of the linked list

    #This method will print the Linked List
    def print(self):
        if self.head == None :
            print('The Linked List is empty')
        else :
            #Fetch the head of the Linked List
            itr = self.head
            llist = ''

            while itr :
                llist += str(itr.element) + '-->'
                itr = itr.nxtPointer # Now the pointer of head will lead you to next node.
            print (llist)

    


# Example usage of the LinkedList class
if __name__ == '__main__' :
    llist = LinkedList()
    llist.add_from_end(5)
    llist.add_from_end(10)
    llist.add_from_end(15)
    llist.add_from_end(20)
    llist.add_from_front(0)
    llist.print()