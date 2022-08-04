# WRITE DATA IN FILE

msg = """
Hello, my name is aniket.
Actually i don't really like programming, but if Chintu can develop app at the age 11.
Then, why i can't create a program for file handling.
"""

f = open("demo.txt", "w")   # if it is not exist, then it will automatically create
f.write(msg)
f.close()

# READ DATA FROM FILE
f = open("demo.txt", "r")   # if it is not exist, then it will show an error(FileNotFoundError)
print(f.read())