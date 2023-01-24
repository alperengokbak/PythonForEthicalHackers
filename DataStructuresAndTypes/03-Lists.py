numbers = [1, 2, 3]
numbers[0] = 2
print(numbers[0])

numbers.append(7)
print(numbers)

# This function pop the last element and display what popped element.
print(numbers.pop())
print(numbers)

# We can create mixed list, so you can add string and integer values at the same time.
mixed = [18, 25, "EA"]
print(mixed)

numbers2 = [4, 5, 6]
result = numbers + numbers2  # We can addition two list between each other.
print(result)

#! Nested lists
newList = [1, 4, "a", [3, "c"]]  # Create a new list inside a list.
print(newList[3])
# We can reach element of the list, inside of primary list.
print(newList[3][0])
print(newList[2:])  # Display same result as like strings.
print(newList[:2])
