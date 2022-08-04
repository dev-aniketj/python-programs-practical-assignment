num = int(input("Enter the number : "))
# checking Palindrome Number or Not
temp, rev_num = num, 0
while num > 0:
    last_digit = num % 10
    rev_num = (rev_num * 10) + last_digit
    num //= 10
print("Palindrome Number") if (rev_num == temp) else print("Not a Palindrome Number")
