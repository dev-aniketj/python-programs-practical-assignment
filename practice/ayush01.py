list = input("Enter the string :").split()

def func(list):
    # str to int
    for i in range(len(list)):
        list[i] = int(list[i])
        print(list[i], "is Even") if (list[i] % 2 == 0) else print(list[i], "is Odd")

func(list)