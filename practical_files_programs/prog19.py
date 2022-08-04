N = int(input("Enter the N : "))
# sum, avg = 0, 0
# for i in range(1, N + 1):
#     sum += i
# avg = sum / N

avg = (N*(N+1)) / (2*N)

print(f"The average of first {N} natural numbers is {avg:.2f}")
