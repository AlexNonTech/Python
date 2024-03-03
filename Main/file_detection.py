import os

path = 'C:\\Users\\ki23-\\OneDrive\\Робочий стіл\\Python\\Main'

if os.path.exists(path):
    print("This location is exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("This location doesn't exist")
