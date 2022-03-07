#wa python program to calulate the length of the string and save that length to the file data.txt
length=str(len(input("Enter string: ")))
file = open("data.txt","w")
data=file.write(length)

file = open("data.txt","r")
data=file.read()
print(data)