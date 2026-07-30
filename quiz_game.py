print("===================================")
print("     Welcome to Python Quiz Game")
print("===================================")

questions = [
    {
        "question": "1. Python kis ne banayi?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Elon Musk"],
        "answer": "B"
    },
    {
        "question": "2. Python kis type ki language hai?",
        "options": ["A. Programming Language", "B. Operating System", "C. Browser", "D. Database"],
        "answer": "A"
    },
    {
        "question": "3. Python file ka extension kya hota hai?",
        "options": ["A. .html", "B. .java", "C. .py", "D. .css"],
        "answer": "C"
    },
    {
        "question": "4. User se input lene ke liye konsa function use hota hai?",
        "options": ["A. print()", "B. input()", "C. len()", "D. type()"],
        "answer": "B"
    },
    {
        "question": "5. Python mein loop kaun sa hota hai?",
        "options": ["A. for", "B. while", "C. Dono", "D. None"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"])

print("\n===================================")
print("          Quiz Finished")
print("===================================")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent! Perfect Score.")
elif percentage >= 80:
    print("Very Good!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Better Luck Next Time!")