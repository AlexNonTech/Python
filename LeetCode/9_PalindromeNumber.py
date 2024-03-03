number = int(input("Enter wanted value: "))


def isPalindrome(x):
    x = str(x)
    if len(x) <= 1:
        return True
    if x[0] == x[-1]:
        return isPalindrome(x[1:-1])
    return False


ispalindrome = isPalindrome(number)
print(ispalindrome)