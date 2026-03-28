import pygame

class pallet:
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
        if keys[pygame.K_SPACE]:
            print("test") # delete later

    def draw(self):
        pygame.draw.rect(self.surface, "white", (self.position.x, self.position.y, self.width, self.height))

    def display_score(self):
        pass

class ball:
    def __init__(self, surface, position, side):
        self.surface = surface
        self.position = position
        self.side = side
        self.played = False

    def move():
        pass

    def draw(self):
        pygame.draw.rect(self.surface, "white", (self.position.x, self.position.y, self.side, self.side))

screen_width = 1280
screen_height = 720

pallet_width = 30
pallet_height = 140

ball_side_size = 20

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

player_starting_position = pygame.Vector2(screen.get_width() - (screen.get_width()-60), (screen.get_height() / 2) - pallet_height / 2)
enemy_starting_position = pygame.Vector2(screen.get_width() -60-pallet_width, (screen.get_height() / 2) - pallet_height / 2)

player = pallet(screen, player_starting_position, pallet_width, pallet_height)
enemy = pallet(screen, enemy_starting_position, pallet_width, pallet_height)
ball = ball(screen,pygame.Vector2(800,400),ball_side_size)

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
        ball.draw()
        pygame.display.flip()

        delta = clock.tick(60) / 1000
    pygame.quit()

main()