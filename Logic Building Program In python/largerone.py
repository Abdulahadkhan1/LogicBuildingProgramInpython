def LARGEST_NUMBER():
    a = int(input("Enter The First numbers : "))
    b = int(input("Enter The Second numbers : "))
    if a < b:
        print(f"{b} is the largest number")
    elif a > b:
        print(f"{a} is the largest number")
    else:
        print(" same numbers ")
if __name__ == "__main__":
    LARGEST_NUMBER() 