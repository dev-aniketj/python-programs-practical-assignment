list1 = [1, 2, 3]
# 1
list1.append(4)
print(list1)  # [1,2,3,4]

# 2
list2 = [5, 6]
list1.extend(list2)
print(list1)  # [1,2,3,4,5,6]

# 3
list1.insert(2, 7)
print(list1)  # [1,2,7,3,4,5,6]

# 4 remove() - remove the element
list1.remove(7)
list1.remove(4)
print(list1)  # [1,2,3,5,6]

# 5 pop() - remove the ele using the index, by default pop element from the end.
list1.pop()
list1.pop(1)
print(list1)  # [1,3,5]

# 6 count() - check the similar element number of times occurance in the list
list2 = [1, 2, 3, 2, 3, 2, 2]
print(list2.count(2))  # 4
print(list2.count(3))  # 2

# 7 index() - find the index of the element, element first time occur in the list.
list1 = [3, 2, 1, 4, 3]
print(list1.index(1))  # 2

# 8 clear() - it is use to clear the list.
list1.clear()
list2.clear()
print(list1)  # []
print(list2)  # []

# 9 sort() - it use to sort the similar dataType elements.
list_number = [5, 2, 4, 1, 3]
list_number.sort()
print(list_number)
list_number.sort(reverse=True)
print(list_number)
