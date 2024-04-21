# Linked List

In this module we will talk about a better method to implement list function . It's called linked list. Basically in lists , you use indexing to traverse the arrays , but in linked list you use links to traverse the array. It's just like following railway compartments. 

![Linked list](image.png)

as you can check in the image that a s ingle data element is called `head` . It contains information or the value of the data of current head and a pointer to the location of the next head. Same goes for the next head. The pointer location in the last head is genrally empty.

## Benefits of linked list over normal list 

- *Dynamic data structure:* A linked list is a dynamic arrangement so it can grow and shrink at runtime by allocating and deallocating memory. So there is no need to give the initial size of the linked list.
- *No memory wastage:* In the Linked list, efficient memory utilization can be achieved since the size of the linked list increase or decrease at run time so there is no memory wastage and there is no need to pre-allocate the memory.
- *Implementation:* Linear data structures like stacks and queues are often easily implemented using a linked list.
- *Insertion and Deletion Operations:* Insertion and deletion operations are quite easier in the linked list. There is no need to shift elements after the insertion or deletion of an element only the address present in the next pointer needs to be updated. 
- *Flexible:* This is because the elements in Linked List  are not stored in contiguous memory locations unlike the array.
- *Efficient for large data:* When working with large datasets linked lists play a crucial role as it can grow and shrink dynamically.
- *Scalability:* Contains the ability to add or remove elements at any position.