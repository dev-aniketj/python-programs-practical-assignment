num = int(input("Enter the number : "))

# check Prime Number or NOT

if num < 2:
    print("It is not a Prime Number")
elif num == 2:
    print("It is a Prime Number")
else:
    flag = False
    for x in range(2, num):
        if num % 2 == 0:
            flag = False
            break
        else:
            flag = True
    print("It is a Prime Number") if flag else print("It is not a Prime Number")
