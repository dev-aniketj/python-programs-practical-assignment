n = int(input("Enter the number : "))
a = 2
b = 5


def func(a, b):
    for i in range(a, b + 1):
        print(n, 'x', i, '=', n * i)


func(a, b)
