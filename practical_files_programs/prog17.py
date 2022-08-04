ch = input("Enter the character : ")
if 48 <= ord(ch[0]) <= 57:
    print(f"Entered '{ch[0]}' is a Digit.")
elif (65 <= ord(ch[0]) <= 90) or (97 <= ord(ch[0]) <= 122):
    print(f"Entered '{ch[0]}' is a Character.")
else:
    print("Invalid value.")
