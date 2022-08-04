# Palindrome function
def palindrome(num):
    rev, temp = 0, num
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    print("Yes, it is a Palindrome number.") if (rev == temp) else print("No, it is not a Palindrome number.")


palindrome(121)
palindrome(153)
palindrome(252)