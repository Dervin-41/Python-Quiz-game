def quiz_game():
    questions = [
        {
            "question": "What is Kanyakumari famous for?",
            "options": ["a) Beaches", "b) Mountains", "c) Deserts", "d) Forests"],
            "answer": "a"
        },
        {
            "question": "In which state is Kanyakumari located?",
            "options": ["a) Kerala", "b) Karnataka", "c) Tamil Nadu", "d) Andhra Pradesh"],
            "answer": "c"
        },
        {
            "question": "What is the name of the statue located in Kanyakumari?",
            "options": ["a) Mahatma Gandhi Statue", "b) Vivekananda Rock Memorial", "c) Thiruvalluvar Statue", "d) Buddha Statue"],
            "answer": "c"
        },
        {
            "question": "Kanyakumari is situated at the confluence of how many seas?",
            "options": ["a) One", "b) Two", "c) Three", "d) Four"],
            "answer": "c"
        },
        {
            "question": "Which festival is prominently celebrated in Kanyakumari?",
            "options": ["a) Pongal", "b) Holi", "c) Navratri", "d) Diwali"],
            "answer": "a"
        },
        {
            "question": "What is the other name of Kanyakumari?",
            "options": ["a) Cape Comorin", "b) Malabar Coast", "c) Coromandel Coast", "d) Marina Beach"],
            "answer": "a"
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer: ").lower()
        if answer == q['answer']:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz_game()
