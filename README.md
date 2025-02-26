# Homework_5

Heap Sort Implementation 

This repository features a python-based implementation of the Heap sort algorithm.
**'max_heapify(arr, n, i)':**
The subtree rooted at index 'i' adheres to the max-heap property.
**'build_max_heap(arr)':**
The constructs a maximum heap from a given arrays of elements.
**'heapsort(arr)':**
The Heap sort algorithm organizes an array in ascending order through a systematic process of heaplification and sorting.
**'main()':**
* Facilitates user input for a numerical list.
* Constructs and displays the Max Heap.
* Outputs the sorted arrays post-Heap sort execution.

python3 Heap_sort.py
Enter numbers separated by spaces: 142 543 123 65 453 879 572 434 111 242 811 102
Max Heap: 142, 543, 123, 65, 453, 879, 572, 434, 111, 242, 811, 102
Heapsort: 65, 102, 111, 123, 142, 242, 434, 453, 543, 572, 811, 879

Binary Search Tree (BST) Implementation
This repository features a python implementation of a binary search tree, encompassing essential operations inclding insertion, deletion and various traversal methods. 

**'Treenode' class: 
* A node in the binary serach tree is characterized by a value('val')and references to its left and right child nodes.
* * BST Operations:**
  * 'add(root, val)' : Introduces a new code containing the specified value into the binary search tree(BST)
  * 'delete(root, val)': Removes a node with the specified value from the binary search tree(BST)
  * 'inorder_traversal(root)':Excecutes an in-order traversal of the binary search tree(BST)
  * 'preorder_traversal(root)':Conducts a pre-order traversal of the binary search tree(BTS)
  * 'find_mind(node)':Identifies the node with the minimum value within a subtree, applicable during detection.
**User Interaction:**
*The 'main()' function offers a straightforward command-line interface.
* It accepts a space-separated sequence of number to construct the BST.
* It displays the in-order traversal of the generated BST.
* It requests the user to input a value for deletion.
* It shows the pre-order traversal of the BST post-deletion, nothing the existence of the deleted value.
In order Bst_operations.py 
python3 Bst_operations.py
Enter numbers separated by spaces: 144 547 123 65 456 870 578 435 112 445 819 101
in-order traversal: 65, 101, 112, 123, 144, 435, 445, 456, 547, 578, 819, 870, 
input a value to delete: 888
pre-order traversal after deletion (888 doesn't exist): 144, 123, 65, 112, 101, 547, 456, 435, 445, 870, 578, 819,
python3 Bst_operations.py
Enter numbers separated by spaces: 144 547 123 65 456 870 578 435 112 445 819 101
in-order traversal: 65, 101, 112, 123, 144, 435, 445, 456, 547, 578, 819, 870, 
input a value to delete: 547
pre-order traversal after deletion (547 is deleted): 144, 123, 65, 112, 101, 578, 456, 435, 445, 870, 819, 
