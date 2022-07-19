num, flag = int(input("Enter the number : ")), False
#check Prime Number or NOT
for x in range(2, num):
    if num%2==0:
        break
    else:
        flag = True
print("It is a Prime Number") if(flag) else print("It is not a Prime Number")

