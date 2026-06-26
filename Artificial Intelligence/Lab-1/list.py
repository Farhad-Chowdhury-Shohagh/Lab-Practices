
numbers = [10, 20, 30, 40, 20]

print("Original List:", numbers)

# append()
numbers.append(50)
print("\nAfter append(50):", numbers)

# insert()
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

# extend()
extra_numbers = [60, 70]
numbers.extend(extra_numbers)
print("After extend([60, 70]):", numbers)

# remove()
numbers.remove(20)   # removes first occurrence
print("After remove(20):", numbers)

# pop()
removed_item = numbers.pop(2)
print("After pop(2):", numbers)
print("Removed Item:", removed_item)

# pop without index
numbers.pop()
print("After pop():", numbers)

# count()
count_20 = numbers.count(20)
print("\nCount of 20:", count_20)

# index()
print("Index of 30:", numbers.index(30))

# sort()
numbers.sort()
print("\nAfter sort():", numbers)

# descending sort
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# copy()
new_list = numbers.copy()
print("\nCopied List:", new_list)

# len()
print("Length of list:", len(numbers))

# max()
print("Maximum value:", max(numbers))

# min()
print("Minimum value:", min(numbers))

# sum()
print("Sum of elements:", sum(numbers))

# clear()
numbers.clear()
print("\nAfter clear():", numbers)
