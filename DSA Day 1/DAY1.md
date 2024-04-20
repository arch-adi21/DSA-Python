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

## Big O notation for Array in python

Python uses dynamic array . In dynamic array whenever you just try to access the index , it will always take a constant time to access any index . But whenever you try to access something elementwise , let's say find the index of 'a' in list [d,c,b,a] . The programme will iterate over each index and compare the elements in that index with the elements present at that index. This means checking over an element in a list in worst case scenario takes `O(n)` time in general.