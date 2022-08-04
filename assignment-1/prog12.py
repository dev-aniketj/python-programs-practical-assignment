name = "Aniket"
# 1.
print(name.lower())  # aniket

# 2.
print(name.isupper())  # False

# 3.
print(name.startswith('a'))  # False
print(name.startswith('A'))  # True
print(name.startswith('Ani'))  # True

# 4.
list1 = ['how', 'are', 'you', '?']
print('\t\t'.join(list1))  # how are you ?

# 5.
sentence = "my name is aniket"
list2 = sentence.split();
print(list2)  # ['my', 'name', 'is', 'aniket']

# 6.
print(name.rjust(20, "*"))  # **************Aniket

# 7.
print(name.center(11, "*"))  # *******Aniket*******
print('hello'.center(10, '*'))

# 8.
sentence2 = '###Hello##World###'
print(sentence2.lstrip('#'))  # Hello##World###
print(sentence2.rstrip('#'))
print(sentence2.strip('#'))
