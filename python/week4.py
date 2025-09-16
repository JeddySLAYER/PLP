import sys

filename = input("enter the file name : ")

try :
    with open(filename) as file : data = file.read()
    print(data)

except FileNotFoundError:
    print("file not found")
    sys.exit()

except PermissionError:
    print("you can't read this file")
    sys.exit()

new_data = input("enter the new data : ")
    
with open("newFile.txt", "w") as file : file.write(new_data)