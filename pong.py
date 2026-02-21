import pygame

class object:
    def __init__(self, surface, position, width, height):
        self.position = position
        self.surface = surface
        self.width = width
        self.height = height

    def keys_pressed(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= 300 * delta
        if keys[pygame.K_s]:
            self.position.y += 300 * delta
    def draw(self):
        pygame.draw.rect(self.surface, "white", (self.position.x, self.position.y, self.width, self.height))


screen_width = 1280
screen_height = 720

object_width = 30
object_height = 140

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Pong")
delta = 0
player_starting_position = pygame.Vector2(screen.get_width() - (screen.get_width()-60), screen.get_height() / 2)
enemy_starting_position = pygame.Vector2(screen.get_width() -60-object_width, screen.get_height() / 2)

player = object(screen, player_starting_position, object_width, object_height)
enemy = object(screen, enemy_starting_position, object_width, object_height)

while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill("black")

    player.draw()
    player.keys_pressed(delta)
    enemy.draw()
    
    
    pygame.display.flip()

    delta = clock.tick(60) / 1000
pygame.quit()