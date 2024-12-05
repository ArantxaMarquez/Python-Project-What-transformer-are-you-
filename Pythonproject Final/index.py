import pygame
import sys
import time
import json 
import os
import random


class TransformerQuiz:
    def __init__(self):
        pygame.init()

         # Screen setup
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Which Transformer are you?")

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.AUTOBOT_RED = (200, 0, 0)
        self.DECEPTICON_PURPLE = (147, 112, 219)
        self.BUTTON_HOVER = (255, 215, 0)
        self.BUTTON_BORDER = (169, 169, 169)

           # Fonts
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

        self.button_radius = 15
        self.button_border_width = 3

         # File handling setup
        self.directory = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.background_image = pygame.image.load("transformer_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        self.overlay = pygame.Surface((self.screen_width, self.screen_height))
        self.overlay.fill(self.WHITE)
        self.overlay.set_alpha(100)



        self.images_directory = os.path.join(self.directory, "images")
        if not os.path.exists(self.images_directory):
            os.makedirs(self.images_directory)

        self.character_images = {}
        self.load_character_images()
    
    
        self.results_file = os.path.join(self.directory, "results.json")
        
        # Load results and initialize scores
        self.results = self.load_results()
        self.scores = self.reset_scores()
        
        self.background_image = pygame.image.load(os.path.join(self.directory, "transformer_background.png"))

        self.overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

    
        self.character_descriptions = {
            "Optimus Prime": "As a natural-born leader, you embody wisdom, courage, and unwavering dedication to protecting others. Like Optimus Prime, you believe in the power of unity and always strive to do what's right, even in the face of great adversity.",
            "Megatron": "Powerful and ambitious, you're not afraid to take charge and pursue your goals with fierce determination. Like Megatron, you have natural leadership abilities and a strong desire to reshape the world according to your vision.",
            "Bumblebee": "Cheerful and loyal, you're the friend everyone can count on. Like Bumblebee, you may be younger or less experienced than others, but your enthusiasm, adaptability, and heart make you an invaluable ally.",
            "Elita-1": "Strong-willed and capable, you're a skilled strategist who leads by example. Like Elita-1, you combine intelligence with combat prowess, and you're never afraid to stand up for what you believe in.",
            "Starscream": "Clever and ambitious, you have a talent for seeing opportunities others miss. Like Starscream, you're not afraid to challenge authority and pursue your own path, though you might need to watch out for overconfidence.",
            "Soundwave": "Silent but observant, you're the one who sees and knows more than others realize. Like Soundwave, you're incredibly loyal to those you trust and possess exceptional analytical abilities.",
            "Shockwave": "Logical and brilliant, you approach problems with cold rationality. Like Shockwave, you excel in scientific pursuits and prefer to base decisions on hard data rather than emotions."
        }


        # Questions and answer mappings remain the same
        self.questions = [ 
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
            },
            {
                "question": "Decepticon or Autobot?",
                "options": ["A) Decepticon", "B) Autobot"]
            },
            {
                "question": "Land or sky?",
                "options": ["A) Land", "B)Sky"]
            },
            {
                "question": "What type of music do you listen to?",
                "options": ["A)Classic", "B)Electronica", "C)Whatever is on the radio", "D)Pop Music", "E)Heavy Metal", "F) I listen to everything :)"]
            },
            {
                "question": "Which “not very good thing” are you most likely to commit?",
                "options": ["A)Coup d'etat", "B)Illegal Racing", "C)Doxxing", "D)Stealing Books", "E)Physical Assault", "F)Illegal experimentation","G)Tax evasion"]
            }
        ]

        self.answer_to_character = [
            {"A": ["Optimus Prime"], "B": ["Megatron"], "C": ["Bumblebee"], "D": ["Elita-1"], "E": ["Starscream"], "F": ["Soundwave"], "G": ["Shockwave"]},
            {"A": ["Optimus Prime", "Bumblebee"], "B": ["Starscream"], "C": ["Megatron", "Starscream", "Shockwave"], "D": ["Elita-1", "Megatron"], "E": ["Bumblebee"]},
            {"A": ["Starscream", "Megatron"], "B": ["Shockwave", "Soundwave"], "C": ["Optimus Prime", "Megatron", "Elita-1"], "D": ["Starscream", "Optimus Prime"]},
            {"A": ["Optimus Prime", "Bumblebee", "Elita-1"], "B": ["Megatron", "Starscream", "Soundwave"], "C": ["Optimus Prime", "Shockwave"]},
            {"A": ["Megatron", "Starscream", "Shockwave", "Soundwave"], "B": ["Optimus Prime", "Bumblebee", "Elita-1"]},
            {"A": ["Optimus Prime", "Bumblebee", "Elita-1", "Shockwave"], "B":["Megatron", "Starscream", "Soundwave"]},
            {"A":["Shockwave", "Optimus Prime"], "B":["Soundwave"], "C":["Optimus Prime", "Bumblebee"], "D":["Bumblebee", "Starscream"], "E":["Megatron", "Optimus Prime"], "F":["Soundwave"]},
            {"A":["Megatron"], "B":["Bumblebee"], "C":["Soundwave"], "D":["Optimus Prime"], "F":["Elita-1"], "G":["Starscream"]}
        ]

    def reset_scores(self):
        return {
            "Optimus Prime": 0,
            "Megatron": 0,
            "Bumblebee": 0,
            "Elita-1": 0,
            "Starscream": 0,
            "Soundwave": 0,
            "Shockwave": 0
        }

    def load_results(self):
        try:
            with open(self.results_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_results(self):
        with open(self.results_file, "w") as file:
            json.dump(self.results, file)

    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)

    

    def wrap_text(self, text, font, max_width):
        lines = []
        words = text.split(' ')
        while words:
            line = ''
            while words and font.size(line + words[0])[0] <= max_width:
                line = line + (words.pop(0) + ' ')
            lines.append(line)
        return lines
    
    def load_character_images(self):
        """Load character images or create placeholders if images don't exist"""

        characters = [
            "Optimus Prime", "Megatron", "Bumblebee", "Elita-1", "Starscream", "Soundwave", "Shockwave"
        ]

        for character in characters:
            # Create filename from character name (replace spaces with underscores)
            filename = f"{character.lower().replace(' ', '_')}.png"
            image_path = os.path.join(self.images_directory, filename)

            try:
                # Try to load the image
                if os.path.exists(image_path):
                    image = pygame.image.load(image_path)
                    # Scale image to reasonable size (e.g., 200x200)
                    image = pygame.transform.scale(image, (200, 200))
                else:
                    # Create a placeholder if image doesn't exist
                    image = pygame.Surface((200, 200))
                    image.fill(self.WHITE)
                    # Draw a border
                    pygame.draw.rect(image, self.BLACK, image.get_rect(), 2)
                    # Add character name to placeholder
                    text = self.small_font.render(character, True, self.BLACK)
                    text_rect = text.get_rect(center=image.get_rect().center)
                    image.blit(text, text_rect)
                
                self.character_images[character] = image

            except pygame.error as e:
                print(f"Error loading image for {character}: {e}")
                # Create placeholder on error
                image = pygame.Surface((200, 200))
                image.fill(self.WHITE)
                pygame.draw.rect(image, self.BLACK, image.get_rect(), 2)
                text = self.small_font.render(character, True, self.BLACK)
                text_rect = text.get_rect(center=image.get_rect().center)
                image.blit(text, text_rect)
                self.character_images[character] = image

    def draw_background(self):

        self.screen.blit(self.background_image, (0,0))

        self.screen.blit(self.overlay, (0,0))


    

    def ask_question(self, question_info, answer_mapping):
        self.draw_background()
        
        # Calculate font sizes dynamically
        question_font_size = min(74, int(self.screen_width / len(question_info["question"]) * 2))
        small_font_size = min(36, int(self.screen_width / 25))
        
        # Dynamic font sizing
        question_font = pygame.font.Font(None, question_font_size)
        small_font = pygame.font.Font(None, small_font_size)

        # Render question with better positioning
        question_surface = question_font.render(question_info["question"], True, self.BLACK)
        question_rect = question_surface.get_rect(centerx=self.screen_width//2, top=20)
        self.screen.blit(question_surface, question_rect)

        # More flexible option container
        option_container_height = min(500, self.screen_height - 150)
        option_container = pygame.Surface((self.screen_width - 100, option_container_height), pygame.SRCALPHA)
        option_container.fill((255, 255, 255, 0))

        # Centered container
        container_rect = option_container.get_rect(
            centerx=self.screen_width//2, 
            top=question_rect.bottom + 20
        )

        # Improved option rendering with dynamic sizing
        option_buttons = []
        option_rects = []
        for i, option in enumerate(question_info["options"]):
            # Dynamically size option buttons
            button_width = min(500, self.screen_width - 150)
            button_height = 50

            # Create base button
            base_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
            base_button.fill(self.AUTOBOT_RED + (230,))  # Add some transparency
            pygame.draw.rect(base_button, self.BUTTON_BORDER, base_button.get_rect(), 3)

            # Render option text
            option_text = small_font.render(option, True, self.WHITE)
            text_rect = option_text.get_rect(center=(button_width//2, button_height//2))
            base_button.blit(option_text, text_rect)

            # Create hover button
            hover_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
            hover_button.fill(self.BUTTON_HOVER + (230,))
            pygame.draw.rect(hover_button, self.BUTTON_BORDER, hover_button.get_rect(), 3)
            hover_button.blit(option_text, text_rect)

            # Vertical spacing
            button_rect = base_button.get_rect(
                centerx=option_container.get_width()//2, 
                top=20 + i * (button_height + 10)
            )

            option_container.blit(base_button, button_rect)
            
            # Adjust rect for screen coordinates
            screen_rect = button_rect.move(container_rect.x, container_rect.y)
            option_rects.append(screen_rect)
            option_buttons.append({
                'base': base_button,
                'hover': hover_button,
                'rect': screen_rect,
                'is_hovered': False
            })

        # Blit the container onto the screen
        self.screen.blit(option_container, container_rect)

        pygame.display.flip()

        #event handling thanks to this the buttons are able to be highlighted when chosen hovered :D
        clock = pygame.time.Clock()
        answered= False
        while not answered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                # Handle hover and click
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    # Reset all buttons to base state
                    for button in option_buttons:
                        if button['is_hovered']:
                            option_container.blit(button['base'], button['rect'].move(-container_rect.x, -container_rect.y))
                            button['is_hovered'] = False

                    # Check for hover
                    for button in option_buttons:
                        if button['rect'].collidepoint(mx, my):
                            option_container.blit(button['hover'], button['rect'].move(-container_rect.x, -container_rect.y))
                            button['is_hovered'] = True

                    # Redraw the container
                    self.screen.blit(option_container, container_rect)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        for i, button in enumerate(option_buttons):
                            if button['rect'].collidepoint(mx, my):
                                answer = chr(ord('A') + i)
                                if answer in answer_mapping:
                                    characters = answer_mapping[answer]
                                    for character in characters:
                                        self.scores[character] += 1
                                    answered = True
                                    break
                
                if event.type == pygame.KEYDOWN:
                    if event.unicode.upper() in answer_mapping:
                        characters = answer_mapping[event.unicode.upper()]
                        for character in characters:
                            self.scores[character] += 1
                        answered = True
                        break 

    def determine_character(self):
        max_score = max(self.scores.values())
        top_scorers = [character for character, score in self.scores.items() if score == max_score]

        if len(top_scorers) > 1:

            final_scores = {character: 0 for character in top_scorers}

            for question_idx, question in enumerate(self.questions):
                answer_mapping = self.answer_to_character[question_idx]
                #Give more weight to later questions
                weight = question_idx + 1

                for answer, characters in answer_mapping.items():
                    for character in characters:
                        if character in top_scorers:
                            final_scores[character] += weight 

            max_weighted_score = max(final_scores.values())
            weighted_winners = [char for char, score in final_scores.items()
                                if score == max_weighted_score]

            if len(weighted_winners) > 1:
                result = [random.choice(weighted_winners)]
            else:
                result = [weighted_winners[0]]
        else:
            result = [top_scorers[0]]

        character = result[0]
        if character in self.results:
            self.results[character] += 1
        else:
            self.results[character] = 1

        self.save_results()

        self.draw_background()
        #Adds a white box behind so descriptions are easier to read
        text_background = pygame.Surface((self.screen_width - 100, self.screen_height), pygame.SRCALPHA)
        text_background.fill((255, 255, 255, 200))

        #position of the white box
        text_background_rect = text_background.get_rect(centerx=self.screen_width//2, top=20)
        self.screen.blit(text_background, text_background_rect)

        result_text =f"You are most like: {', '.join(result)}"
        result_lines = self.wrap_text(result_text, self.small_font, self.screen_width - 100)

        y_offset = 50
        for line in result_lines:
            self.draw_text(line, self.small_font, self.BLACK, 50, y_offset)
            y_offset += self.small_font.get_height() + 5

        for character in result:
            if character in self.character_images:
                image = self.character_images[character]

                image_x = (self.screen_width - image.get_width()) // 2

                image_y = y_offset + 10
                self.screen.blit(image, (image_x, image_y))

                y_offset = image_y + image.get_height() + 20

            description_lines = self.wrap_text(self.character_descriptions[character], self.small_font, self.screen_width - 100)
            for line in description_lines:
                self.draw_text(line, self.small_font, self.BLACK, 50, y_offset)
                y_offset += self.small_font.get_height() + 5
        
        button_continue = pygame.Rect(275, 500, 250, 50)
        pygame.draw.rect(self.screen, self.AUTOBOT_RED, button_continue)
        self.draw_text('Continue', self.small_font, self.BLACK, 355, 515)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mx, my = pygame.mouse.get_pos()
                        if button_continue. collidepoint((mx, my)):
                            waiting = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

        self.screen.blit(result_text, (50, 300))
        pygame.display.flip()
        time.sleep(5)    

    def game(self):
        self.scores = self.reset_scores()
        for i, question in enumerate(self.questions):
            self.ask_question(question, self.answer_to_character[i])
        self.determine_character()

    def stats_screen(self):
        running = True
        while running:
            self.draw_background()
            
            title_lines = self.wrap_text('Character Stats', self.font, self.screen_width - 100)
            y_offset = 50
            for line in title_lines:
                self.draw_text(line, self.font, self.BLACK, 80, y_offset)
                y_offset += self.font.get_height() + 10

            stats_y_offset = y_offset + 20
            current_results = self.load_results()
            for character, count in current_results.items():
                stat_text = f"{character}: {count} times"
                self.draw_text(stat_text, self.small_font, self.BLACK, 50, stats_y_offset)
                stats_y_offset += self.small_font.get_height() + 5

            button_back = pygame.Rect(275, 500, 250, 50)
            pygame.draw.rect(self.screen, self.AUTOBOT_RED, button_back)
            self.draw_text('Back', self.small_font, self.BLACK, 375, 515)

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_back.collidepoint((mx, my)):
                            running = False
                            return

            pygame.display.update()

    def draw_button(self, rect, text, text_color, base_color, border_color, hover=False):
        """Draw a custom button with rounded corners, border, and hover effect"""
        mx, my = pygame.mouse.get_pos()

        if rect.collidepoint((mx, my)) or hover:
            color = self.BUTTON_HOVER
        else:
            color = base_color
        #draw rounded button
        pygame.draw.rect(self.screen, border_color, rect, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, color, rect.inflate(-self.button_border_width, -self.button_border_width), border_radius=self.button_radius)

        gradient = pygame.Surface((rect.width - self.button_border_width*2, rect.height//2))
        gradient.fill(self.WHITE)
        gradient.set_alpha(30)
        self.screen.blit(gradient, (rect.x + self.button_border_width, rect.y + self.button_border_width))

        text_surface = self.small_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            self.draw_background()

            title_lines = self.wrap_text('What Transformer Are You?', self.font, self.screen_width - 100)
            y_offset = 50
            for line in title_lines:
                self.draw_text(line, self.font, self.BLACK, 80, y_offset)
                y_offset += self.font.get_height() + 10

            button_width = 300
            button_height = 60
            button_x = (self.screen_width - button_width) // 2

            start_button = pygame.Rect(button_x, 200, button_width, button_height)
            stats_button = pygame.Rect(button_x, 300, button_width, button_height)
            quit_button = pygame.Rect(button_x, 400, button_width, button_height)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(275, 200, 250, 50)
            button_2 = pygame.Rect(275, 300, 250, 50)
            button_3 = pygame.Rect(275, 400, 250, 50)

            pygame.draw.rect(self.screen, self.AUTOBOT_RED, button_1)
            pygame.draw.rect(self.screen, self.DECEPTICON_PURPLE, button_2)
            pygame.draw.rect(self.screen, self.AUTOBOT_RED, button_3)

            self.draw_text('Start Quiz', self.small_font, self.WHITE, 290, 215)
            self.draw_text('Stats', self.small_font, self.WHITE, 370, 315)
            self.draw_text('Quit', self.small_font, self.WHITE, 370, 410)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if start_button.collidepoint(event.pos):
                            self.game()
                        elif button_2.collidepoint(event.pos):
                            self.stats_screen()
                        elif button_3.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    quiz = TransformerQuiz()
    quiz.main_menu()