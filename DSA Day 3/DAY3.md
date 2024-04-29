# Doubly Linked List

In this section we will talk about doubly linked list in detail. Doubly Linked List is an example of Singly Linked List , or let's just say , Linked List. In Linked List we had a reference pointer in each node , which pointed to the next node , but there was no provision for node to point backwards. So if a person was on current node and he needed to access the previous node , he need to do a new traversal . To solve this issue , we will use Doubly Linked List , which contains one more reference along with the `next` reference and this extra reference is called `previous`.

![Doubly Linked List](image.png)

In the picture you can clearly see that we have two reference items now. For the head , the `previous` pointer will remain null. For the last / tail node , the next pointer will remain empty.

## Inserting an element at the front

- Like we did in the Singly Linked List , first we need to create a node with empty `previous` , `element` and `next`.
- As there is no previous node at the front , we need to assign null to the `previous` reference of new node being inserted at the front
- Update the element entered by the user
- The `next` reference will refer to the previous head , which we just now replaced with a new node.
- The `previous` of the previous head which we just now replaced with the new node , needs to be updated by replacing the null with the reference to the new node. 

## Inserting an element at the end

- Create a new node with `next` as Null , `element` as the input by the user , and `previous` will be assigned with a reference to the previous last node , which you will now replace.
- In this scenario , you need to traverse the whole Linked List structure at the very minimum requirement.
- When you reach at the end , the `next` reference of the current last node will now upadated while pointing to a new last node which you created before traversing . 

## Insertion at any desired index

- You must be aware that for inserting at any desired location , the user won't give any particular address , rather he will givex an index , just like an array . Now it's our duty to keep a count of number of nodes we traversed , so that we can mimic a index.
- Initiate a node with `previous` and `next` as Null , and assign the user input to `element`.
- Start traversing the array , while maitaining a count (starting from 1 for head) , and when your count is to the index , this means that this node will be the previous node after we insert the desired node. Change the `next` of this node to refer the new node which we created .
- Update `previous` of new node to the location of this node at the required index.
- Update the `next` of this new node to the `next` of the current node at required index. :) Well done