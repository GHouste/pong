import pygame

class object:
    def __init__(self, surface, position, width, height):
        self.position = position
        self.surface = surface
        self.width = width
        self.height = height
        self.points = 0

    def keys_pressed(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.position.y >= 0:
            self.position.y -= 300 * delta
        if keys[pygame.K_s] and self.position.y <= screen_height - self.height:
            self.position.y += 300 * delta

    def draw(self):
        pygame.draw.rect(self.surface, "white", (self.position.x, self.position.y, self.width, self.height))

    def display_score(self):
        pass

screen_width = 1280
screen_height = 720

object_width = 30
object_height = 140

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

player_starting_position = pygame.Vector2(screen.get_width() - (screen.get_width()-60), (screen.get_height() / 2) - object_height / 2)
enemy_starting_position = pygame.Vector2(screen.get_width() -60-object_width, (screen.get_height() / 2) - object_height / 2)

player = object(screen, player_starting_position, object_width, object_height)
enemy = object(screen, enemy_starting_position, object_width, object_height)

def main():
    running = True
    delta = 0
    while running == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.fill("black")

        pygame.draw.rect(screen, "white", (screen_width / 2, 0, 3 ,screen_height))
        player.draw()
        player.keys_pressed(delta)
        enemy.draw()
        
        pygame.display.flip()

        delta = clock.tick(60) / 1000
    pygame.quit()

main()