# Create an empty list
my_list = []

# Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending elements:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at position 2:", my_list)

# Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Sort in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)