string = input("Enter the string : ")

# lower()
print("lower() :", string.lower())

# upper()
print("upper() :", string.upper())

# islower()
print("islower() :", string.islower())

# isupper()
print("isupper() :", string.isupper())

# startswith()
print("startswith('m') :", string.startswith('m'))

# endswith
print("endswith('.') :", string.endswith('.'))

# join()
list = string.split()
print("join() :", "->".join(list))

# split()
list = string.split()
print("split() :", list)

# rjust()
print("rjust() :", string.rjust(30))

# ljust()
print("ljust() :", string.ljust(30))

# center()
print("center() :", string.center(30))

# lstrip()
print("lstrip('my') :", string.lstrip("my"))

# rstrip()
print("rstrip('.') :", string.rstrip('.'))

# reverse()
list = string.split()
list.reverse()
print("reverse() :", " ".join(list))
