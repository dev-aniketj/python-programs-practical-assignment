# input_string = input("Enter elements of a list separated by space : ")
# list = input_string.split()     #str format

list = input("Enter elements of a list separated by space : ").split()     #str format

# 1. converting str to int
for i in range(len(list)):
    list[i] = int(list[i])
print("List : ", list)

# 2. display the count occurance of each number
print("Element in a List at number of times :")
for i in range(len(list)):
    print(list[i], " : ", list.count(list[i]), "time")

# 3. create two lists , even & odd numbers.
evenList, oddList = [], []
for i in range(len(list)):
    if list[i] % 2 == 0:
        evenList.append(list[i])
    else:
        oddList.append(list[i])

print("Even List : ", evenList)
print("Odd List : ", oddList)
