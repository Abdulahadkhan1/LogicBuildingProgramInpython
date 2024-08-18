def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
         print(num1-num2)
def mul(num1,num2):
          print(num1 * num2)
def div(num1,num2):
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero.")


def main():
    while True:
        print("Calculator")
        print("1. Addition ")
        print("2. Subtraction ")
        print("3. Multiplication ")
        print("4. Division ")
        print("5. Exit ")
        choice = input("Enter Your Choice : ")
        
        if choice == '5':
            print("Exiting the program.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        new_func(choice , num1,num2)

def new_func(choice, num1, num2):
    match choice:
     case '1':
          add(num1,num2)
     case '2':
         sub(num1,num2)
     case '3':
          mul(num1,num2)
     case '4':
        div(num1,num2)
     case _:
            print("Invalid choice.")
if __name__ == "__main__":
 main()