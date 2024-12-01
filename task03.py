def main():
    # Define questions with options and answers
    questions = {
        "What is the capital of France?": {
            "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
            "answer": "1"
        },
        "What is 5 + 3?": {
            "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
            "answer": "3"
        },
        "Which programming language is known as Python?": {
            "options": ["1. C", "2. Python", "3. Java", "4. JavaScript"],
            "answer": "2"
        },
        "Who wrote 'To Kill a Mockingbird'?": {
            "options": ["1. J.K. Rowling", "2. Harper Lee", "3. Ernest Hemingway", "4. Mark Twain"],
            "answer": "2"
        },
        "What is the largest planet in our solar system?": {
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": "3"
        },
        "The Central Rice Research Station is situated in?": {
            "options": ["1. Chennai", "2. Cuttack", "3. Bangalore", "4. Quilon"],
            "answer": "2"
        },
         "The metal whose salts are sensitive to light is?": {
            "options": ["1. Zinc", "2. Silver", "3. Copper", "4. Aluminum"],
            "answer": "2"
        },
         "Patanjali is well known for the compilation of –": {
            "options": ["1. Yoga Sutra", "2. Panchatantra", "3. Nrahma Sutra", "4. Ayurveda"],
            "answer": "1"
        },
          "The country that has the highest in Barley Production?": {
            "options": ["1. China", "2. India", "3. Russia", "4. France"],
            "answer": "3"
        },
            "D.D.T. was invented by?": {
            "options": ["1. Mosley", "2. Rudolf", "3. Karl Benz", "4. DAlton"],
            "answer": "1"
        }
    }

    score = 0

    print("Welcome to the Quiz Application!")
    print("Answer the following questions:\n")

    for question_number, (question, data) in enumerate(questions.items(), start=1):
        print(f"Question {question_number}: {question}")
        for option in data["options"]:
            print(option)
        
        while True:
            user_answer = input("Your answer (enter the number): ").strip()

            if not user_answer.isdigit() or int(user_answer) < 1 or int(user_answer) > len(data["options"]):
                print("Invalid input! Please enter a number between 1 and 4.\n")
            else:
                break
        if user_answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_option = data["options"][int(data["answer"]) - 1]
            print(f"Incorrect! The correct answer was: {correct_option}\n")

    print(f"Quiz completed! Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
