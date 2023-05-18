import pygame
import sys

#window settings
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIN_rect = WIN.get_rect()

#player setting
player_image = pygame.image.load("aart\_rocket.png")
player_image.set_colorkey(player_image.get_at((0, 0)))
player_rect = player_image.get_rect()
player_rect.center = (WIN_rect.centerx, 500)
player_velocity = 1

def enlarge_image(image, colorkey = None, amount = 2):
    new_image = pygame.transform.scale(image, (image.get_width() / amount, image.get_height() / amount))
    if colorkey != None:
        if colorkey == -1:
            colorkey = new_image.get_at((0,0))
        new_image.set_colorkey(colorkey, pygame.RLEACCEL)
    return new_image

#enemy settings
enemy_velocity = 1
enemy_image = pygame.image.load("aart\_alien.png")
enemy_image = enlarge_image(enemy_image, -1)
enemy_image.set_colorkey(enemy_image.get_at((0, 0)))
enemy_rect = enemy_image.get_rect()

#bullet settings
bullets = pygame.sprite.Group()

class missile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image =  enlarge_image(pygame.image.load("aart\_missile.png"), amount=3)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        

bullets.add(missile((50, 50)), missile((300, 300)))
while True:
    enemy_rect.x += 5 *enemy_velocity
    if enemy_rect.right > WIN_rect.right:
        enemy_velocity = -1
    if enemy_rect.left < WIN_rect.left:
        enemy_velocity = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit
                pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_rect.y -= 5 * player_velocity
    if keys[pygame.K_a]:
        player_rect.x -= 5 * player_velocity
    if keys[pygame.K_s]: 
        player_rect.y += 5 * player_velocity
    if keys[pygame.K_d]: 
        player_rect.x += 5 * player_velocity
    if keys[pygame.K_SPACE]:
        missile += 5
        player_rect.y -= 5
    if player_rect.colliderect(enemy_rect):
        enemy_velocity, player_velocity = 0, 0
    
    WIN.fill((60, 40, 70))
    WIN.blit(player_image, player_rect)
    WIN.blit(enemy_image, enemy_rect)
    bullets.draw(WIN)

    pygame.display.update()