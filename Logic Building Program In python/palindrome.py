def is_palindrome():
    user_input = input("Enter the value : ")

    processed_string = ''.join(char.lower() for char in user_input if char.isalnum())

    if processed_string == processed_string[::-1]:
        print("the value is palindrome")
    else :
        print("not palindrome")
if __name__ == "__main__":
    is_palindrome()