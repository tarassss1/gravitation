import pygame
pygame.init()

class Player:
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.gravity = 0.5
        self.jump_power = -10
        self.vel_y = 0
        self.can_jump = False

    def move(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.vel_y > 0:
                    self.rect.bottom = w.rect.top
                    self.vel_y = 0
                    self.can_jump = True
                elif self.vel_y < 0:
                    self.rect.top = w.rect.bottom
                    self.vel_y = 0

    def jump(self):
        if self.can_jump:
            self.vel_y = self.jump_power
            self.can_jump = False

    def move_horizontal(self, dx):
        self.rect.x += dx
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left

                elif dx < 0:
                    self.rect.left = wall.rect.right


class Wall:
    def __init__(self, x, y, width, height, color=(22, 26, 31)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# створення персонажа
player = Player(100, 100, 50, 50, 'bird.png')

# створення стін
walls = [
    Wall(350, 250, 200, 400),
    Wall(275, 300, 150, 400),
    Wall(250, 275, 50, 400),
    Wall(125, 250, 50, 600),
    Wall(0, 200, 50, 450),
    Wall(100, 120, 75, 20),
    Wall(250, 0, 50, 150),
    Wall(375, 0, 25, 250)
]

# кольори
white = (255, 255, 255)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
move_left = False
move_right = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False

    window.fill(white)
    player.move()

    if move_right:
        player.move_horizontal(3)
    if move_left:
        player.move_horizontal(-3)

    for wall in walls:
        wall.draw(window)

    window.blit(player.image, (player.rect.x, player.rect.y))

    clock.tick(60)
    pygame.display.update()

pygame.quit()
