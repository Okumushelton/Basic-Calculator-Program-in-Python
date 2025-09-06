# This program demonstrates a series of common list operations in Python.

# Step 1: Create an empty list called my_list.
my_list = []

# Step 2: Append elements to the list.
# The append() method adds an item to the end of the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# The list is now [10, 20, 30, 40]

# Step 3: Insert a value at a specific position.
# The insert() method takes two arguments: the index and the value.
my_list.insert(1, 15)

# The list is now [10, 15, 20, 30, 40]

# Step 4: Extend the list with another list.
# The extend() method adds all items from an iterable (like another list) to the end.
my_list.extend([50, 60, 70])

# The list is now [10, 15, 20, 30, 40, 50, 60, 70]

# Step 5: Remove the last element.
# The pop() method removes and returns the last item in the list.
my_list.pop()

# The list is now [10, 15, 20, 30, 40, 50, 60]

# Step 6: Sort the list in ascending order.
# The sort() method sorts the list in place.
my_list.sort()

# The list is now [10, 15, 20, 30, 40, 50, 60]

# Step 7: Find and print the index of a specific value.
# The index() method returns the index of the first occurrence of a value.
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Optional: Print the final list to see all the changes.
print("The final list is:", my_list)
