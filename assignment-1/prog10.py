# input_string = input("Enter elements of a list separated by space : ")
# lst = input_string.split()     #str format

lst = input("Enter elements of a list separated by space : ").split()     #str format

# 1. converting str to int
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("List : ", lst)

# 2. display the count occurrence of each number
print("Element in a List at number of times :")
for i in set(lst):
    print(i, " : ", lst.count(i), "time")

# 3. create two lists , even & odd numbers.
evenList, oddList = [], []
for i in lst:
    if i % 2 == 0:
        evenList.append(lst[i])
    else:
        oddList.append(lst[i])

print("Even List : ", evenList)
print("Odd List : ", oddList)
