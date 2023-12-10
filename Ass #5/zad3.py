import pygame
import random
import os

pygame.init()

# Kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

# Ścieżka do pliku z najwyższym wynikiem
HIGHSCORE_FILE_PATH = "highscore.txt"

class Rakietka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move(self, pixels):
        self.rect.x += pixels
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 690:
            self.rect.x = 690

class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [random.choice([-4, 4]), 4]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x >= 690 or self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]

        if self.rect.y > 490 or self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]

def read_highscore():
    if os.path.exists(HIGHSCORE_FILE_PATH):
        with open(HIGHSCORE_FILE_PATH, 'r') as file:
            return int(file.read())
    return 0

def write_highscore(score):
    with open(HIGHSCORE_FILE_PATH, 'w') as file:
        file.write(str(score))

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietka = Rakietka(BIALY, 100, 10)
rakietka.rect.x = 300
rakietka.rect.y = 490

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = 345
pileczka.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

# Główna pętla gry
continue_game = True
clock = pygame.time.Clock()
score = 0
highscore = read_highscore()

while continue_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietka.move(-5)
    if keys[pygame.K_RIGHT]:
        rakietka.move(5)

    all_sprites_list.update()

    if pygame.sprite.collide_mask(pileczka, rakietka):
        pileczka.velocity[1] = -pileczka.velocity[1]
        score += 1

    if pileczka.rect.y > 490:
        if score > highscore:
            highscore = score
            write_highscore(highscore)
        print(f"Game Over! Score: {score}, Highscore: {highscore}")
        score = 0
        pileczka.rect.x = 345
        pileczka.rect.y = 195

    screen.fill(CZARNY)
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}   Highscore: {highscore}", 1, BIALY)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
