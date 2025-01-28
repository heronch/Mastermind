import pygame 

WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
BROWN = (139, 69, 19)  
RED = (255, 0, 0)  
BLUE = (0, 0, 255)  
GREEN = (0, 255, 0) 
YELLOW = (255, 255, 0)  
PURPLE = (128, 0, 128)  
ORANGE = (255, 165, 0)  

color_names = {
    RED: "Red",
    BLUE: "Blue",
    GREEN: "Green",
    YELLOW: "Yellow",
    PURPLE: "Purple",
    ORANGE: "Orange"
}

def draw_board(screen, mastermind_instance):
    screen.fill(BROWN) 
    for i in range(mastermind_instance.max_guesses): 
        for j in range(4): 
            pygame.draw.rect(screen, WHITE, (j * 50 + 50, i * 50 + 50, 40, 40))  
            pygame.draw.rect(screen, BLACK, (j * 50 + 50, i * 50 + 50, 40, 40), 1)  
        if i < len(mastermind_instance.guess_history): 
            guess = mastermind_instance.guess_history[i]  
            for j in range(4):  
                pygame.draw.rect(screen, guess[j], (j * 50 + 50, i * 50 + 50, 40, 40)) 
            
            black_pegs, white_pegs = mastermind_instance.guess_results[i]  
            for b in range(black_pegs):
                    pygame.draw.circle(screen, BLACK, (250 + b * 20, i * 50 + 50), 10)  
            for w in range(white_pegs):
                    pygame.draw.circle(screen, WHITE, (250 + black_pegs * 20 + w * 20, i * 50 + 50), 10)  

def draw_colors(screen, colors):
    for i, color in enumerate(colors):  
        pygame.draw.rect(screen, color, (i * 50 + 350, 50, 40, 40))  
        pygame.draw.rect(screen, BLACK, (i * 50 + 350, 50, 40, 40), 1)  

    pygame.draw.rect(screen, BLACK, (650, 450, 100, 40))  
    pygame.draw.rect(screen, WHITE, (650, 450, 100, 40), 1) 
    render_text(screen, "Clear", 675, 460) 
    
    pygame.draw.rect(screen, BLACK, (650, 500, 100, 40))  
    pygame.draw.rect(screen, WHITE, (650, 500, 100, 40), 1)  
    render_text(screen, "Save", 675, 510)  

    pygame.draw.rect(screen, BLACK, (650, 550, 100, 40))
    pygame.draw.rect(screen, WHITE, (650, 550, 100, 40), 1)  
    render_text(screen, "Load", 675, 560)  

def render_text(screen, text, x, y):
    font = pygame.font.Font(None, 36) 
    text_surface = font.render(text, True, WHITE)  
    screen.blit(text_surface, (x, y)) 
