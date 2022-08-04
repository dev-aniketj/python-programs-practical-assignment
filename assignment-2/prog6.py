def secondLargest(*args):
    try:
        args_list = list(args)
        args_list.sort(reverse=True)
        for i in range(len(args_list)):
            args_list[i] / args_list[i]  # for checking the list as int or str
        return args_list[1]
    except:
        return 'Please enter the integer values.'


print(secondLargest(1, 5, 3, 4, 2))
print(secondLargest('a', 'b'))
