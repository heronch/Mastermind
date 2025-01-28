import pygame  
import random  
import pickle  
from sprites import draw_board, draw_colors, render_text, WHITE, BLACK, BROWN, RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, color_names  

class Mastermind:
    def __init__(self):
        self.colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]  
        self.pattern = random.sample(self.colors, 4) 
        self.guesses = 0  
        self.max_guesses = 10  
        self.saved_game = None  
        self.guess_results = []  
        self.guess_history = [] 

    def load_game(self):
        try:
            with open('saved_game.pkl', 'rb') as f:  
                self.saved_game = pickle.load(f) 
                self.pattern = self.saved_game['pattern']  
                self.guesses = self.saved_game['guesses']  
                self.guess_results = self.saved_game.get('guess_results', [])  
                self.guess_history = self.saved_game.get('guess_history', [])  
        except FileNotFoundError:
            print("No saved game found. Starting a new game.") 

    def save_game(self):
        with open('saved_game.pkl', 'wb') as f:  
            pickle.dump({'pattern': self.pattern, 'guesses': self.guesses, 'guess_results': self.guess_results, 'guess_history': self.guess_history}, f)  

    def check_guess(self, guess):
        black_pegs = 0 
        white_pegs = 0  
        pattern_copy = self.pattern.copy() 
        guess_copy = guess.copy()  

        for i in range(4): 
            if guess[i] == self.pattern[i]: 
                black_pegs += 1 
                pattern_copy[i] = None  
                guess_copy[i] = None 

        for color in guess_copy:  
            if color is not None and color in pattern_copy:  
                white_pegs += 1  
                pattern_copy[pattern_copy.index(color)] = None  
        self.guess_results.append((black_pegs, white_pegs))  
        return black_pegs, white_pegs 

    def play(self):
        pygame.init() 
        screen = pygame.display.set_mode((800, 600))  
        clock = pygame.time.Clock() 
        running = True 
        current_guess = [] 

        # Start a new game
        self.pattern = random.sample(self.colors, 4) 
        self.guesses = 0 
        self.guess_results = [] 
        self.guess_history = []

        while running:  # Main game loop
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    running = False  
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if 650 < event.pos[0] < 750 and 500 < event.pos[1] < 540:
                        self.save_game()
                    elif 650 < event.pos[0] < 750 and 450 < event.pos[1] < 490:
                        current_guess = []  
                    elif 650 < event.pos[0] < 750 and 550 < event.pos[1] < 590:
                        self.load_game() 
                    else:
                        for i, color in enumerate(self.colors):  
                            if 350 + i * 50 < event.pos[0] < 390 + i * 50 and 50 < event.pos[1] < 90: 
                                current_guess.append(color)  
                elif event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_RETURN:
                        if len(current_guess) == 4: 
                            self.guess_history.append(current_guess.copy())  
                            black_pegs, white_pegs = self.check_guess(current_guess)  
                            self.guesses += 1  
                            draw_board(screen, self)  
                            if black_pegs == 4:  
                                render_text(screen, "Congratulations! You won!", 50, 550)  
                                pygame.display.flip() 
                                pygame.time.wait(6000)  
                                running = False 
                            elif self.guesses == self.max_guesses:
                                pattern_words = ', '.join([color_names[color] for color in self.pattern]) 
                                render_text(screen, f"Game over! The pattern was: {pattern_words}", 50, 550)  
                                pygame.display.flip() 
                                pygame.time.wait(6000)  
                                running = False  
                            current_guess = [] 
                    elif event.key == pygame.K_s:  
                        self.save_game()  

            draw_board(screen, self) 
            draw_colors(screen, self.colors) 
            
            pygame.draw.rect(screen, BLACK, (650, 450, 100, 40))  
            pygame.draw.rect(screen, WHITE, (650, 450, 100, 40), 1) 
            render_text(screen, "Clear", 675, 460)  

            for i, color in enumerate(current_guess): 
                pygame.draw.circle(screen, color, (i * 50 + 370, 120), 20)  
                pygame.draw.circle(screen, BLACK, (i * 50 + 370, 120), 20, 1) 

            pygame.display.flip() 
            clock.tick(60) 

        pygame.quit()  

if __name__ == "__main__": 
    game = Mastermind() 
    game.play()  