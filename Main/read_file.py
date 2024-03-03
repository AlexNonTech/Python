try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found :(")

print("\nis file closed?: " + str(file.closed))
