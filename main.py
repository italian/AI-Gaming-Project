import pygame  # используется для создания игры
import sys  # чтобы использовать метод sys.exit() для завершения программы
import random  # для генерации случайных чисел

# Инициализация Pygame
pygame.init()  # Инициализирует все модули Pygame

# Настройки экрана
screen_width = 800
screen_height = 600
# Создает окно игры с заданными размерами
screen = pygame.display.set_mode((screen_width, screen_height))
# Устанавливает заголовок окна игры
pygame.display.set_caption("Neural Adventure")

# Основные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.SysFont("tahoma", 55)


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        Конструктор класса, инициализирует объект игрока.
        """
        super().__init__()  # Вызывает конструктор базового класса Sprite
        # Создает поверхность размером 50x50 пикселей для отображения игрока
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)  # Заполняет поверхность черным цветом
        # Создает прямоугольник для игрока на основе его изображения
        self.rect = self.image.get_rect()
        # Устанавливает начальную позицию игрока в центре экрана
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5  # Устанавливает скорость движения игрока

    def update(self):
        """
        Метод обновления состояния игрока, обрабатывает ввод с клавиатуры.
        """
        # Получает текущее состояние всех клавиш
        keys = pygame.key.get_pressed()
        if (
            keys[pygame.K_LEFT] or keys[pygame.K_a]
            and self.rect.left > 0
        ):
            self.rect.x -= self.speed
        if (
            keys[pygame.K_RIGHT] or keys[pygame.K_d]
            and self.rect.right < screen_width
        ):
            self.rect.x += self.speed
        if (
            keys[pygame.K_UP] or keys[pygame.K_w]
            and self.rect.top > 0
        ):
            self.rect.y -= self.speed
        if (
            keys[pygame.K_DOWN] or keys[pygame.K_s]
            and self.rect.bottom < screen_height
        ):
            self.rect.y += self.speed


# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """
        Конструктор класса, инициализирует объект врага.
        """
        super().__init__()  # Вызывает конструктор базового класса Sprite
        # Создает поверхность размером 50x50 пикселей для отображения врага
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)  # Заполняет поверхность красным цветом
        # Создает прямоугольник для врага на основе его изображения
        self.rect = self.image.get_rect()
        # Генерирует случайную позицию врага на экране
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        """
        Метод обновления состояния врага.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Проверка выхода врага за границы экрана
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y


# Создание группы спрайтов
# Создает группу спрайтов для управления и обновления всех спрайтов в игре
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()  # Создает группу спрайтов врагов

player = Player()  # Создает экземпляр игрока
all_sprites.add(player)  # Добавляет игрока в группу спрайтов

# Создание врагов
for _ in range(5):
    enemy = Enemy()  # Создает экземпляр врага
    all_sprites.add(enemy)  # Добавляет врага в группу спрайтов
    enemies.add(enemy)  # Добавляет врага в группу спрайтов


# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    """
    Draws the given text onto the specified surface at the given coordinates
    using the specified font and color.

    :param text: The text to be drawn.
    :type text: str
    :param font: The font to be used for drawing the text.
    :type font: pygame.font.Font
    :param color: The color of the text.
    :type color: tuple
    :param surface: The surface onto which the text will be drawn.
    :type surface: pygame.Surface
    :param x: The x-coordinate of the center of the text.
    :type x: int
    :param y: The y-coordinate of the center of the text.
    :type y: int
    :return: None
    """
    textobj = font.render(text, True, color)  # Renders the text
    textrect = textobj.get_rect()  # Gets the dimensions of the text
    textrect.center = (x, y)  # Centers the text
    surface.blit(textobj, textrect)  # Draws the text


# Игровой цикл
running = True  # Переменная, управляющая циклом игры
game_over = False  # Переменная, показывающая, что игра окончена
while running:
    # Обрабатывает все события в очереди событий Pygame
    for event in pygame.event.get():
        # Завершает игру, если окно закрыто
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Обновление состояния игры
        all_sprites.update()  # Обновляет состояние всех спрайтов в группе

        # Проверка столкновений игрока с врагами
        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True
            print("Game over!")

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка объектов
    all_sprites.draw(screen)  # Отрисовывает все спрайты на экране

    if game_over:
        draw_text(
            "Game over!",
            font,
            BLACK,
            screen,
            screen_width // 2,
            screen_height // 2,
            )

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров до 60 FPS
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()  # Останавливает все модули Pygame
sys.exit()  # Завершает программу
