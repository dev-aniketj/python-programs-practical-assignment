nums = input("Enter the numbers : ").split()
for i in range(len(nums)):
    #str to int
    nums[i] = int(nums[i])

    #condition
    if (nums[i] > 500):
        break
    elif (nums[i] > 150 and nums[i] <= 500):
        continue
    elif (nums[i] % 5 == 0):
        print(nums[i])
