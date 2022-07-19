test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
dict_list = {i: list(str(i) * test_list.count(i)) for i in test_list}
print(dict_list)