import pygame

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Pong")
delta = 0
player_position = pygame.Vector2(screen.get_width() - (screen.get_width()-60), screen.get_height() / 2)
enemy_position = pygame.Vector2(screen.get_width() -60, screen.get_height() / 2)


while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill("black")
    pygame.draw.circle(screen, "white", player_position, 20)
    pygame.draw.circle(screen, "white", enemy_position, 20)
    if keys[pygame.K_w]:
        player_position.y -= 300 * delta
    if keys[pygame.K_s]:
        player_position.y += 300 * delta
    
    pygame.display.flip()

    delta = clock.tick(60) / 1000
pygame.quit()