from collections import defaultdict

lst = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
res = defaultdict(list)
for i in lst:
    res[i].append(i)
print(dict(res))
