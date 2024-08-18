import random

def guess_the_number():
    number_to_guess = random.randint(1,10)
    attempt = 0
    guessed = False
    while not guessed:
        try:
            user_guess =  int(input("Enter The number you have gussed : "))  
            attempt += 1 

            if user_guess < number_to_guess:
              print("you have gussesd too low")
            elif user_guess > number_to_guess:
              print("you have gussed too high")
            else :
              guessed = True
              print(f"Congratulations! You guessed the number in {attempt} attempts.")
        except ValueError:
           print("invalid value")
if __name__ == "__main__":
   guess_the_number()