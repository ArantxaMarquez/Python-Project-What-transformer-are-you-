import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000,900 ))
pygame.display.set_caption("Which Transformer Are You?")

# Define font
font = pygame.font.Font(None, 36)

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
        "question": "Choose a positive trait you identify with:",
        "options": ["A) Kind", "B) Ambitious", "C) Optimistic", "D) Hardworking", "E) Cunning", "F) Loyal", "G) Intelligent"]
    },
    {
        "question": "Choose a negative trait you identify with:",
        "options": ["A) Naive", "B) Cowardly", "C) Cruel", "D) Stubborn", "E) Unattentive"]
    },
    {
        "question": "Pick one genre of movie:",
        "options": ["A) Soap Opera", "B) Horror", "C) Action", "D) Romance"]
    },
    {
        "question": "What do you think is the most significant issue society is currently facing?",
        "options": ["A) Separation", "B) Inequality", "C) Ignorance"]
    }
]

# Define the mapping of answers to characters
answer_to_character = [
    {"A": ["Optimus Prime"], "B": ["Megatron"], "C": ["Bumblebee"], "D": ["Elita-1"], "E": ["Starscream"], "F": ["Soundwave"], "G": ["Shockwave"]},
    {"A": ["Optimus Prime", "Bumblebee"], "B": ["Starscream"], "C": ["Megatron", "Starscream", "Shockwave"], "D": ["Elita-1", "Megatron"], "E": ["Bumblebee"]},
    {"A": ["Starscream", "Megatron"], "B": ["Shockwave", "Soundwave"], "C": ["Optimus Prime", "Megatron", "Elita-1"], "D": ["Starscream", "Optimus Prime"]},
    {"A": ["Optimus Prime", "Bumblebee", "Elita-1"], "B": ["Megatron", "Starscream", "Soundwave"], "C": ["Optimus Prime", "Shockwave"]}
]

def ask_question(question_info, answer_mapping):
    screen.fill((255, 255, 255))
    question_text = font.render(question_info["question"], True, (0, 0, 0))
    screen.blit(question_text, (50, 50))

    y_offset = 150
    for option in question_info["options"]:
        option_text = font.render(option, True, (0, 0, 0))
        screen.blit(option_text, (100, y_offset))
        y_offset += 50

    pygame.display.flip()
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.unicode.upper() in answer_mapping:
                    characters = answer_mapping[event.unicode.upper()]
                    for character in characters:
                        scores[character] += 1
                    answered = True

def determine_character():
    max_score = max(scores.values())
    result = [character for character, score in scores.items() if score == max_score]
    screen.fill((255, 255, 255))
    result_text = font.render(f"You are most like: {', '.join(result)}", True, (0, 0, 0))
    screen.blit(result_text, (50, 300))
    pygame.display.flip()
    time.sleep(5)  # Pause to display the result

# Run the quiz
for i, question in enumerate(questions):
    ask_question(question, answer_to_character[i])

determine_character()

pygame.quit()
