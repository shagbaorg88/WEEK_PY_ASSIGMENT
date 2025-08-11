Key List Operations Explained
Creating Lists:

my_list = [] creates an empty list

Appending Elements:

append() adds an element to the end of the list

Time complexity: O(1) average case

Inserting Elements:

insert(index, element) adds an element at a specific position

Time complexity: O(n) as elements need to be shifted

Extending Lists:

extend(iterable) adds all elements from another iterable to the end

Time complexity: O(k) where k is the length of the new elements

Removing Elements:

pop() removes and returns the last element

pop(i) can remove an element at a specific index

Time complexity: O(1) for last element, O(n) for arbitrary element

Sorting Lists:

sort() sorts the list in-place in ascending order

Time complexity: O(n log n)

Finding Elements:

index(element) returns the first index of the specified element

Time complexity: O(n) worst case

Raises ValueError if element not found

How to Run
Save the code in a file named list_operations.py

Run the program using Python:

text
python list_operations.py
Requirements
Python 3.x

This program demonstrates fundamental list operations in Python and serves as a good introduction to list manipulation techniques.

New chat
