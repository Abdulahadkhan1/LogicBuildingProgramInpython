import random 

def rock_paper_scissor():
    while True:
        user = input("Enter a choice (rock, paper, scissor): ").lower()
        choices = ['rock' , 'paper' ,'scissor']
        computer = random.choice(choices)
        if user not in choices:
            print("Invalid input. Please enter rock, paper or scissor.")

        if user == 'rock':
            if computer == 'scissor':
                print("rock smashes scissor, you win!")
            elif computer == 'paper':
                print("paper covers rock, you lose!")
            else:
                print("Draw")
        elif user == 'paper':
            if computer == 'rock':
                print("paper covers rock, you win!")
            elif user == 'scissor':
                print("scissor cuts paper, you lose!")
            else:
                print("draw")
        elif user == 'scissor':
            if computer == 'paper':
                print("scissor cuts paper, you win!")
            elif computer == 'rock':
                print("rock smashes scissor, you lose!")
            else :
                print("draw")

if __name__ == "__main__":
    rock_paper_scissor()