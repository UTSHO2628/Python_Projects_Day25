import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Bird settings
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
BIRD_COLOR = BLUE
BIRD_GRAVITY = 0.5
BIRD_JUMP = -10
BIRD_DOWN = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Bird Jump Game")

# Fonts
font = pygame.font.Font(None, 36)

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.color = BIRD_COLOR
        self.velocity = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.velocity += BIRD_GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = BIRD_JUMP

    def move_down(self):
        self.velocity = BIRD_DOWN

# Main game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    running = True
    game_over = False

    while running:
        clock.tick(30)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_PAGEUP:  # Jump with Page Up
                    bird.jump()
                if event.key == pygame.K_PAGEDOWN:  # Move down with Page Down
                    bird.move_down()

        if not game_over:
            bird.update()

            # Check if the bird hits the ground or flies off screen
            if bird.y + BIRD_HEIGHT > SCREEN_HEIGHT or bird.y < 0:
                game_over = True

        bird.draw()

        # Display Game Over message
        if game_over:   
            game_over_text = font.render("Game Over! Press R to Restart", True, BLACK)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

        pygame.display.flip()

        # Restart the game if 'R' is pressed
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    main()  # Restart the game

    pygame.quit()

if __name__ == "__main__":
    main()
