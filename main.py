import pygame  # используется для создания игры
import sys  # чтобы использовать метод sys.exit() для завершения программы.

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
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed


# Создание группы спрайтов
# Создает группу спрайтов для управления и обновления всех спрайтов в игре
all_sprites = pygame.sprite.Group()
player = Player()  # Создает экземпляр игрока
all_sprites.add(player)  # Добавляет игрока в группу спрайтов

# Игровой цикл
running = True  # Переменная, управляющая циклом игры
while running:
    # Обрабатывает все события в очереди событий Pygame
    for event in pygame.event.get():
        # Завершает игру, если окно закрыто
        if event.type == pygame.QUIT:
            running = False

    # Обновление состояния игры
    all_sprites.update()  # Обновляет состояние всех спрайтов в группе

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка объектов
    all_sprites.draw(screen)  # Отрисовывает все спрайты на экране

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров до 60 FPS
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()  # Останавливает все модули Pygame
sys.exit()  # Завершает программу
