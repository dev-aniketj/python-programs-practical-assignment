def sum(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    return a + b + c + d + e + f + g + h


print(sum())
print(sum(1))
print(sum(1, 2))
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4))


def sub(a, b):
    return a - b


print(sub(1))
print(sub(1,2,3))
# it shows error bcoz we can't assign para. with default value (=0),
# and no. of arguments are not matched.
