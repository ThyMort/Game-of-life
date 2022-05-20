import pygame, sys



display_width = 800
display_height = 600
welcomeScreen = pygame.display.set_mode((display_width, display_height))

red = (255, 0, 0)
white = (255, 255, 255)

welcomeScreen.fill(white, rect = None, special_flags = 0)

welcomeFont = pygame.font.Font(None, 50)


welcomeMessageBackground = pygame.draw.rect(welcomeScreen, red, [200, 100, 400, 75]) 

welcomeMessage = welcomeFont.render('Welcome! Click a button to get started.', True, white, red)
welcomeScreen.blit(welcomeMessage, (70, 100))


pygame.display.update()











pygame.init()

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

class Button():
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
        self.call_back_ = action
    def draw(self):
        self.mouseover()
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)
    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouseover colol
    def call_back(self):
        self.call_back_()
def my_great_function():
    print("Great! " * 5)
def my_fantastic_function():
    print("Fantastic! " * 5)
def mousebuttondown():
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()
screen = pygame.display.set_mode((120, 100))
RED = (255, 0, 0)
BLUE = (0, 0, 255)

button_01 = Button("Great!", (60, 30), my_great_function)
button_02 = Button("Fantastic!", (60, 70), my_fantastic_function, bg=(50, 200, 20))
buttons = [button_01, button_02]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown()
    for button in buttons:
        button.draw()
 
    pygame.display.flip()
    pygame.time.wait(40)
