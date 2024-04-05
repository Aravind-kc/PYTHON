import quiz as q

score = 0
    
for question in q.quiz():
        print(question["question"])
        answer = input("Your answer: ")
        question_answer = question["answer"]
        if answer == question_answer:
            print("wow!!Correct!")
            score += 1
        else:
            print("sorry!!Wrong!")
    
print(f"Quiz complete! You scored {score} out of {len(q.quiz())}")

q.quiz()