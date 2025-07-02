import pygame

pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Button test")
Screen.fill((255, 255, 255))

Butt_On_Img = pygame.image.load('Images/Butt On_Btn.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        Screen.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()
        Action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                Action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return Action

Butt_On_Btn = Button(96, 152, Butt_On_Img, 0.5)

Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    if Butt_On_Btn.draw():
        print ('Working')

    pygame.display.update()
    fps = 60

pygame.quit()