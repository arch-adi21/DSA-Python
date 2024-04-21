# Linked List

In this module we will talk about a better method to implement list function . It's called linked list. Basically in lists , you use indexing to traverse the arrays , but in linked list you use links to traverse the array. It's just like following railway compartments. 

![Linked list](image.png)

as you can check in the image that a single data element is called `Node` . The first node in any LinkedList is called `head` . It contains information or the value of the data of current head and a pointer to the location of the next head. Same goes for the next head. The pointer location in the last head is genrally empty.

## Benefits of linked list over normal list 

- *Dynamic data structure:* A linked list is a dynamic arrangement so it can grow and shrink at runtime by allocating and deallocating memory. So there is no need to give the initial size of the linked list.
- *No memory wastage:* In the Linked list, efficient memory utilization can be achieved since the size of the linked list increase or decrease at run time so there is no memory wastage and there is no need to pre-allocate the memory.
- *Implementation:* Linear data structures like stacks and queues are often easily implemented using a linked list.
- *Insertion and Deletion Operations:* Insertion and deletion operations are quite easier in the linked list. There is no need to shift elements after the insertion or deletion of an element only the address present in the next pointer needs to be updated. 
- *Flexible:* This is because the elements in Linked List  are not stored in contiguous memory locations unlike the array.
- *Efficient for large data:* When working with large datasets linked lists play a crucial role as it can grow and shrink dynamically.
- *Scalability:* Contains the ability to add or remove elements at any position.

## How to create a Linked list in python

Linked list is not a default data type for python . For a linked list , you need to use your own logic to create a data structure. In this section i will give you a breif break-down on how to create your own linked list.

```python

# Using a class we can create the Node of the LinkedList

class Node :
  
  # We will initiate this Node by defining the element and the pointer through __init__ constructor

  def __init__(self , element = None , nxtPointer = None) :
    
    self.element = element
    self.nxtPointer = nxtPointer
```  
### Creating a LinkedList class

Now that we have our Node class, we can use it to create our LinkedList class. The LinkedList class will have a single head element which points to the first node in the list.

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

### Adding a Node
We can add a node to our linked list by creating a new Node and setting it as the head if the list is empty, or by traversing the list and adding the new Node at the end.

```python

# Create a new class LinkedList , which will use Nodes to store data .

class LinkedList:

    # Initiate the head of the LinkedList
    def __init__(self):
        self.head = None

    #This method will help you to add an element at the head position of the linked list
    def add_from_front(self, element):
        node = Node(element , self.head) # assign a Node to a variable and use the previous head as the pointer
        self.head = node # update the assigned node as the new head. 

    #This method will print the Linked List
    def print(self):
        if self.head == None :
            print('The Linked List is empty')
        else :
            #Fetch the head of the Linked List
            itr = self.head
            llist = ''

            while itr :
                llist = str(itr.data) + '-->'
                itr = self.nxtPointer # Now the pointer of head will lead you to next node.
            print (llist)
```