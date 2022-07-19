# prime func and evenOdd func

def evenOdd(num):
    if (num % 2 == 0):
        print("and even number.")
    else:
        print("and odd number.")


def prime(num):
    flag = False
    for i in range(2, num):
        if (num % i == 0):
            break
        else:
            flag = True
    if (flag):
        print(num, "is prime", end=' ')
    else:
        print(num, "is not prime", end=' ')
    evenOdd(num)


n = int(input("Enter the number : "))
prime(n)
