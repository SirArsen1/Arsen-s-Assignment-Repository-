import pygame, random

class NyanCat(pygame.sprite.Sprite):

    def __init__(self, cat_x, cat_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('nyancat_frames/nyan1.png'))
        self.sprites.append(pygame.image.load('nyancat_frames/nyan2.png'))
        self.sprites.append(pygame.image.load('nyancat_frames/nyan3.png'))
        self.sprites.append(pygame.image.load('nyancat_frames/nyan4.png'))
        self.sprites.append(pygame.image.load('nyancat_frames/nyan5.png'))
        self.sprites.append(pygame.image.load('nyancat_frames/nyan6.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.cat_x = cat_x
        self.cat_y = cat_y

        self.rect = self.image.get_rect()
        self.rect.topleft = [cat_x, cat_y]

    def update(self):
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

Screen_Width = 1200
Screen_Height = 300
BG_Color = (12,78,143)

pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('nyancat')

# img = pygame.image.load("nyancat_frames/nyan1.png").convert_alpha()
moving_sprites = pygame.sprite.Group()
cat_x = random.randint(0, 1250)
cat_y = random.randint(10, 50)
NyanCat = NyanCat(cat_x,cat_y)
moving_sprites.add(NyanCat)

y_dir = 1
y_min = 10
y_max = 50
y_speed = 1

clock = pygame.time.Clock()
flag = True
while flag:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    dist = random.randint(1,10)
    if NyanCat.rect.x < Screen_Width:
        NyanCat.rect.x += dist
    else:
        NyanCat.rect.x = 0

    NyanCat.rect.y += y_dir * y_speed

    if NyanCat.rect.y >= y_max:
        NyanCat.rect.y = y_max
        y_dir = -1
    elif NyanCat.rect.y <= y_min:
        NyanCat.rect.y = y_min
        y_dir = 1

    screen.fill(BG_Color)
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()

pygame.quit()
exit(0)