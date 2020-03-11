#program which contains one function that accept one number from user and
#true if number is divisible by 5 otherwise return false
def five():
    num = input("Enter number :  ")
    if int(num) % 5 == 0:
        print("True")
    else:
        print("False")
five()
