import time

# Initialize scores for each character
scores = {
    "Optimus Prime": 0,
    "Megatron": 0,
    "Bumblebee": 0,
    "Elita-1": 0,
    "Starscream": 0,
    "Soundwave": 0,
    "Shockwave": 0
}

# Define the questions and corresponding options
questions = [
    {
        "question": "Choose a positive trait you identify with:\nA) Kind\nB) Ambitious\nC) Optimistic\nD) Hardworking\nE) Cunning\nF) Loyal\nG) Intelligent",
        "options": {
            "A": "Optimus Prime",
            "B": "Megatron",
            "C": "Bumblebee",
            "D": "Elita-1",
            "E": "Starscream",
            "F": "Soundwave",
            "G": "Shockwave"
        }
    },
    {
        "question": "Choose a negative trait you identify with:\nA) Naive\nB) Cowardly\nC) Cruel\nD) Stubborn\nE) Unattentive",
        "options": {
            "A": ["Optimus Prime", "Bumblebee"],
            "B": [],
            "C": ["Megatron", "Starscream", "Shockwave", "Soundwave"],
            "D": ["Elita-1", "Megatron"],
            "E": []
        }
    },
    # Add more questions as needed
]

def ask_question(question_info):
    print(question_info["question"])
    answer = input("Your choice: ").upper()
    if answer in question_info["options"]:
        characters = question_info["options"][answer]
        if isinstance(characters, list):
            for character in characters:
                scores[character] += 1
        else:
            scores[characters] += 1
    else:
        print("Invalid choice, please select one of the options.")
    time.sleep(1)  # Pause for a moment before the next question

def determine_character():
    max_score = max(scores.values())
    result = [character for character, score in scores.items() if score == max_score]
    print(f"\nYou are most like: {', '.join(result)}")

# Run the quiz
for question in questions:
    ask_question(question)

determine_character()
