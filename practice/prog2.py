name = "AnIket kuMar JaIn"
l = name.split()

for i in range(len(l)-1):
    print(l[i][0].upper() + ".", end=" ")

print(l[len(l)-1][0].upper() + l[len(l)-1][1:].lower())