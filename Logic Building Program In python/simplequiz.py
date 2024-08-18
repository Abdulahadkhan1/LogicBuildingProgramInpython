def questions_answers():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
            "answer": "A"
        }
    ]

    score = 0
    for q in questions:
        print(q["question"])
        for choices in q["choices"]:
            print(choices)
            
        user_answer = input("User Answer can be from ( A  B  C  D ) :")

        if  user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    print(f" Your Total score is {score}/{len(questions)}")

if __name__ == "__main__":
   questions_answers()