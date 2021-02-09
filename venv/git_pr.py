import pygame
import sys
import os

FPS = 50
WINDOW_SIZE = WIDTH, HEIGHT = 500, 900


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    # else:
    #     image = image.convert_alpha()
    return image


class Shoot(pygame.sprite.Sprite):
    image = load_image("bomb.png")

    def __init__(self, x, y, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Shoot.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 1
        self.rect = self.rect.move(self.rect.x, self.rect.y)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    character = load_image("boom.png")
    pygame.display.set_caption("Star wars")
    x = 180
    y = 780
    speed = 4
    count = 0
    process = True
    all_sprites = pygame.sprite.Group()
    while process:
        pygame.time.delay(10)
        pygame.mouse.set_visible(False)
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                count += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - speed > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + speed + 125 < WIDTH:
            x += speed
        for _ in range(count):
            Shoot(x, y, all_sprites)

        screen.blit(character, (x, y))
        pygame.display.update()


if __name__ == "__main__":
    main()
