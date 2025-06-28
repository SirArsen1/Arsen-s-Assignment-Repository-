import pygame, random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Drawing Pal")
screen.fill("white")

fps_clock = pygame.time.Clock()

Instructions_Font = pygame.font.SysFont(None, 24)
Guide_Text_Surface = pygame.Surface((1280, 142))
Guide_Text_Surface.fill((195, 195, 195))

Brush_Surface_1 = pygame.Surface((24, 24), pygame.SRCALPHA)
Brush_Surface_2 = pygame.Surface((24, 24), pygame.SRCALPHA)
Brush_Surface_3 = pygame.Surface((24, 24), pygame.SRCALPHA)

pygame.draw.circle(Brush_Surface_1, (255, 0, 0, 255), (12, 12), 10) # Circle1
pygame.draw.circle(Brush_Surface_2, (0, 255, 0, 255), (12, 12), 10) # Circle2
pygame.draw.circle(Brush_Surface_3, (0, 0, 255, 255), (12, 12), 10) # Circle3

Brush_Shapes_List = (
    Brush_Surface_1, Brush_Surface_2, Brush_Surface_3
)

Brush_Shape_Container = Brush_Surface_1
Drawing = False

class Brush_Class: # brush class

    def __init__(self, Brush_Shape = Brush_Surface_1):
        self._shape_of_brush = Brush_Shape

    def Get_Brush_Shape(self):
        return self._shape_of_brush

    def Set_Brush_Shape(self, Brush_Shape):
        for Brush in Brush_Shapes_List:
            if Brush in Brush_Shapes_List:
                self._shape_of_brush = Brush_Shape

    def Draw(self, Screen_Surface, Screen_Position):
        Brush_Surface = self._shape_of_brush
        rect = Brush_Surface.get_rect(center=Screen_Position)
        Screen_Surface.blit(Brush_Surface, rect)


Drawing_Brush = Brush_Class()

def Instruction_Guide_Text():
    Guide_Text_Line1 = Instructions_Font.render(("Welcome to Drawing Pal!"), True, (0, 0, 0))
    Guide_Text_Line2 = Instructions_Font.render((">You can draw using left button of your mouse. You can draw by just clicking or dragging while holding the left button."), True, (0, 0, 0))
    Guide_Text_Line3 = Instructions_Font.render((">To change your brush press 1, 2, or 3."), True, (0, 0, 0))
    Guide_Text_Line4 = Instructions_Font.render((">To clean canvas press C button on your keyboard"), True, (0, 0, 0))

    screen.blit(Guide_Text_Line1, (10, 10))
    screen.blit(Guide_Text_Line2, (10, 34))
    screen.blit(Guide_Text_Line3, (10, 58))
    screen.blit(Guide_Text_Line4, (10, 82))

def Brush_Display():

    Brush_Display_Text = Instructions_Font.render(("Current brush: "), True, (0, 0, 0))
    screen.blit(Brush_Display_Text, (10, 106))
    screen.blit(Brush_Shape_Container, (128, 103))

def Control_Logic_Keys(Keys):
    global Brush_Shape_Container

    if Keys[pygame.K_1]:  # Brush 1
        Drawing_Brush.Set_Brush_Shape(Brush_Surface_1)
        Brush_Shape_Container = Brush_Surface_1
    elif Keys[pygame.K_2]:  # Brush 2
        Drawing_Brush.Set_Brush_Shape(Brush_Surface_2)
        Brush_Shape_Container = Brush_Surface_2
    elif Keys[pygame.K_3]:  # Brush 3
        Drawing_Brush.Set_Brush_Shape(Brush_Surface_3)
        Brush_Shape_Container = Brush_Surface_3
    elif Keys[pygame.K_c]:  # fills the screen with white color
        screen.fill("white")

def Control_Logic_Mouse(event):
    global Drawing

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            Drawing = True
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            Drawing = False

def main():
    Run = True
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

            Keys = pygame.key.get_pressed()
            Control_Logic_Keys(Keys)
            Control_Logic_Mouse(event)

        if Drawing:
            mouse_pos = pygame.mouse.get_pos()
            Drawing_Brush.Draw(screen, mouse_pos)

        screen.blit(Guide_Text_Surface, (0, 0))
        Instruction_Guide_Text()
        Brush_Display()

        fps_clock.tick(60)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

pygame.quit()