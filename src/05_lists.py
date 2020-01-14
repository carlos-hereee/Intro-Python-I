# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("\n Adds 4 to the end: ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("\n Combines array x and y: ", x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.extend((8, 9, 10))
print("\n add 8, 9, 10 to array x: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(6, 99)
print("\n Add 99 in array x: ", x)

# Print the length of list x
# YOUR CODE HERE
print("\n Length of list: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
n = [i * 1000 for i in x]
print("\n Multiplied by 1000", n)
