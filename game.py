import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Drag Image Here")
clock = pygame.time.Clock()

# 允许 DROPFILE 事件
pygame.event.set_allowed([pygame.QUIT, pygame.DROPFILE])

image = None
image_rect = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.DROPFILE:
            print("Dropped file:", event.file)
            try:
                image = pygame.image.load(event.file).convert_alpha()
                image = pygame.transform.scale(image, (200, 200))
                image_rect = image.get_rect(center=(400, 300))
            except:
                print("Unsupported file!")

    screen.fill((50, 50, 80))
    if image:
        screen.blit(image, image_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
