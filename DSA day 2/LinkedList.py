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

    def length(self):
        count = 0 # initiate a counter
        itr = self.head
        while itr :
            count += 1 # increment the counter
            itr = itr.nxtPointer
        return count
    
    def remove_element(self, index):
        if index < 0 or index >= self.length() :
            raise Exception('Invalid Index') # If the index is invalid , raise an exception
        if index == 0 :
            self.head = self.head.nxtPointer # If the index is 0 , then update the head to the next node
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1 :
              itr.nxtPointer = itr.nxtPointer.nxtPointer # If the index is found , then update the pointer of the previous node to the next node
              break
            itr = itr.nxtPointer
            count += 1

    def insert_at(self, index, element):
        if index < 0 or index >= self.length() :
            raise Exception('Invalid Index')
        if index == 0 :
            self.add_from_front(element) # If the index is 0 , then add the element at the front
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1 :
                node = Node(element , itr.nxtPointer) # If the index is found , then add the element at the index
                itr.nxtPointer = node # Update the pointer of the previous node to the new node
                break
            itr = itr.nxtPointer
            count += 1

    def insert_values(self, list_of_elements):
        self.head = None # Empty the linked list
        for elements in list_of_elements : # iterate through the list of elements
            self.add_from_end(elements) # add the elements in the end sequentially 

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
    


# Example usage of LinkedList
if __name__ == '__main__' :
    ll = LinkedList()
    ll.add_from_end(5)
    ll.add_from_end(10)
    ll.add_from_end(15)
    ll.add_from_end(20)
    ll.add_from_end(25)
    ll.print()
    print(ll.length())
    ll.remove_element(2)
    ll.print()
    ll.insert_at(2, 15)
    ll.print()
    ll.insert_values([1,2,3,4,5])
    ll.print()