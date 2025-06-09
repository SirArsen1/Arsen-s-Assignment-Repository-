import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Drawing Pal")
fps_clock = pygame.time.Clock()
BG_color = (255, 255, 255)

Brush_Font_Container = None # container for default font, "None" so that it can fill it later
for font_name in ["Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", None]:
    try:
        brush_font_name = pygame.font.SysFont(font_name, 40)
        test_font = brush_font_name.renderer("@", True, (0,0,0))
        if test_font.get_width() > 0: # checks if symbol is more than zero and actually rendered
            Brush_Font_Container = brush_font_name
            break
    except Exception:
        continue

Brush_Font = pygame.font.SysFont(Brush_Font_Container, 40)
print(f"Using {Brush_Font_Container} brush")

class Brush_Class: # brush class
    def __init__(self, font_symbol = "@"):
        self._symbol_for_brush = font_symbol
    def get_brush_symbol(self):
        return self._symbol_for_brush
    def set_brush_symbol(self, font_symbol):
        if isinstance(font_symbol, str) and font_symbol.strip() != "": # checks if brush is string and is a part of brush set, also if it's not empty
            self._symbol_for_brush = font_symbol
    def draw (self, surface, position):
        try:
            font_surface = Brush_Font.render(self._symbol_for_brush, True, (0,0,0))
            if font_surface.get_width() == 0: # checks if symbol is actually rendered
                raise ValueError ("Symbol should not be empty")
        except Exception:
            font_surface = Brush_Font.render("?", False, (0,0,0))
        rect = font_surface.get_rect(center=position) #rect = rectangle
        surface.blit(font_surface, rect)

Drawing_Brush = Brush_Class()
Drawing = False
Instructions_Font = pygame.font.SysFont(None, 24)

while True:
    for event in pygame.event.get():
        # === Quit Event ===
        if event.type == pygame.quit: # closing game event
            pygame.quit()
            sys.exit()

        #=== Mouse ===
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse press is left click
            if event.button == 1: # using binary logic 1 = yes, 0 = no
                Drawing = True # therefore 1 = True in this case
        elif event.type == pygame.MOUSEBUTTONUP: # checks if right click is used
            if event.button == 1:
                Drawing = False # in this case we don't want right click to trigger drawing, therefore 1 = False

        #=== Brush and Canvas controls ===
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: # Brush 1
                Drawing_Brush.set_brush_symbol("@")
            elif event.key == pygame.K_2: # Brush 2
                Drawing_Brush.set_brush_symbol("|")
            elif event.key == pygame.K_3: # Brush 3
                Drawing_Brush.set_brush_symbol("_")
            elif event.key == pygame.K_c: # fills the screen with white color
                screen.fill(BG_color)

    if Drawing: # Makes sure that brush is drawing while the left mouse button is held, so while dragging
        mouse_pos = pygame.mouse.get_pos()
        Drawing_Brush.draw(screen, mouse_pos)

    Instruction_Text = Instructions_Font.render(
        "Welcome to Drawing Pal!"
        ">You can draw using left button of your mouse. You can draw by just clicking or dragging while holding the left button."
        ">To change your brush press 1, 2, or 3."
        ">To clean canvas press C button on your keyboard", True, (0,0,0)
    )
    Brush_Display = Instructions_Font.render(f"Current brush: {Drawing_Brush.get_brush_symbol()} ", True, (0,0,0))

    screen.blit(Instruction_Text, (10,10))
    screen.blit(Brush_Display, (10,40))

    pygame.display.update()
    fps_clock.tick(60)