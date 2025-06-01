import pygame

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
# img = pygame.transform.scale(img, (170,105))
moving_sprites = pygame.sprite.Group()
NyanCat = NyanCat(102,63)
moving_sprites.add(NyanCat)

cat_x = 100
cat_y = 100

clock = pygame.time.Clock()
flag = True
while flag:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    if cat_x  < Screen_Width:
        cat_x += 3
    else:
        cat_x = 0

    screen.fill(BG_Color)
    moving_sprites.draw(screen)
    moving_sprites.update()
    #NOW IT DOESN'T MOVE
    pygame.display.flip()

pygame.quit()
exit(0)