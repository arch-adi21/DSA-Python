# Arrays

There are two types of arrays in computing world . Static array and Dynamic array. Languages like C and Java have both type of arrays. But in python , by default we use dynamic array. 

## Example of Dynamic Array :- 
```
import java.util.ArrayList;

public class Main {

  public static void main(String[] args) {
      
    ArrayList<Integer> arr=new ArrayList<>();
    System.out.println(arr.size());
      
  }
}
```

This is an initialisation of dynamic array in Java. To learn more about the memory allocation and management of the Dynamic arrays in Java and C go through clicking here [(JavaPoint tutorials)](https://www.javatpoint.com/dynamic-array-in-java)

## Example of Static Array :- 

```
int a[5] = {1, 2, 3, 4, 5}; //Static Integer Array
int *a = new int[5]; //Dynamic Integer Array
```
Rules of initialising a static array is very simple in any language . Tho it is more simple to start a dynamic array in python.

## Big O notation for 1D Array in python

Python uses dynamic array . In dynamic array whenever you just try to access the index , it will always take a constant time to access any index . But whenever you try to access something elementwise , let's say find the index of 'a' in list [d,c,b,a] . The programme will iterate over each index and compare the elements in that index with the elements present at that index. This means checking over an element in a list in worst case scenario takes `O(n)` time in general.

### Accessing an Element by Index:
- Time Complexity: O(1)
- Space Complexity: O(1)
- Accessing an element in a one-dimensional array by its index is typically a constant-time operation because it directly computes the memory location of the element.

### Inserting an Element at the End:
- Time Complexity: O(1) (Amortized)
- Space Complexity: O(1)
- Inserting an element at the end of a one-dimensional array usually involves updating the array’s size and placing the new element in the next available position, which is a constant-time operation on average.

### Inserting an Element at the Beginning:
- Time Complexity: O(n)
- Space Complexity: O(n)
- Inserting an element at the beginning of a one-dimensional array requires shifting all existing elements to make room, resulting in a linear time and space complexity.

### Searching for an Element (Linear Search):
- Time Complexity: O(n)
- Space Complexity: O(1)
- In the worst case, searching for an element in a one-dimensional array may require looking at every element, resulting in a linear time complexity. The space complexity remains constant.

### Deleting an Element:
- Time Complexity: O(n)
- space complexity: O(1)
- In the worst case, deleting an element from the front may take O(n) time as elements after an element should be shifted by one position. A noticable thing is unlike Insertion , the space complexity here is constant . This is because while deleting a data , the data is not actually deleted . Instead either the location is kept empty or the pointer is removed from that location. So here we don't need any shifting of data

## Big O notation for 2D Array in python

### Accessing an Element by Indices:
- Time Complexity: O(1)
- Space Complexity: O(1)
- Accessing an element in a two-dimensional array using row and column indices is generally a constant-time operation, similar to one-dimensional arrays.

### Inserting an Element at a Specific Position:
- Time Complexity: O(1)
- Space Complexity: O(1)
- Inserting an element at a specific position in a two-dimensional array typically has a constant-time complexity because it directly computes the memory location of the element based on its indices.

### Searching for an Element (Linear Search):
- Time Complexity: O(m * n)
- Space Complexity: O(1)
- When searching for an element in a two-dimensional array, you may need to examine all elements in the worst case, resulting in a time complexity of O(m * n), where ‘m’ is the number of rows and ‘n’ is the number of columns. The space complexity remains constant because , during any search , we don't need any extra memory at all.

### Deleting an Element:
- Time complexity: O(m*n)
- Space complexity: O(1)
- While deleting an element , you may need to search through the whole array which requires O(m*n) time. 

### Transposing a Matrix:
- Time Complexity: O(m * n)
- Space Complexity: O(m * n)
- Transposing a two-dimensional array involves swapping elements across the diagonal. This operation requires examining and potentially swapping all elements which includes two loops of i and j to create a swap , resulting in a time complexity of O(m * n) and a space complexity of O(m * n).




