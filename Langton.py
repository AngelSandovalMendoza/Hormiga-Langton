import pygame
import sys

class LangtonAnt:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False] * width for _ in range(height)]  # False representa el color blanco
        self.ant_position = (width // 2, height // 2)  # La posición inicial de la hormiga
        self.direction = 'up'  # Dirección inicial: arriba

    def turn_ant(self, turn_direction):
        directions = ['up', 'right', 'down', 'left']
        current_direction_index = directions.index(self.direction)
        if turn_direction == 'right':
            self.direction = directions[(current_direction_index + 1) % 4]
        elif turn_direction == 'left':
            self.direction = directions[(current_direction_index - 1) % 4]

    def move_ant(self):
        x, y = self.ant_position
        if self.grid[y][x]:  # Si la casilla está negra
            self.turn_ant('right')
            self.grid[y][x] = False  # Cambiar el color de la casilla a blanco
        else:
            self.turn_ant('left')
            self.grid[y][x] = True  # Cambiar el color de la casilla a negro

        # Mover la hormiga
        if self.direction == 'up':
            self.ant_position = (x, (y - 1) % self.height)
        elif self.direction == 'right':
            self.ant_position = ((x + 1) % self.width, y)
        elif self.direction == 'down':
            self.ant_position = (x, (y + 1) % self.height)
        elif self.direction == 'left':
            self.ant_position = ((x - 1) % self.width, y)

    def draw_grid(self, screen):
        cell_size = min(screen.get_width() // self.width, screen.get_height() // self.height)
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (0, 0, 0) if cell else (255, 255, 255)  # Negro si la casilla está negra, blanco si está blanca
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    def simulate(self, screen, steps):
        for _ in range(steps):
            self.move_ant()
            self.draw_grid(screen)
            pygame.display.flip()  # Actualizar la pantalla

# Configuración de pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Langton Ant Simulation')

# Ejemplo de uso
if __name__ == "__main__":
    langton_ant = LangtonAnt(100, 100)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        langton_ant.simulate(screen, 1)
        clock.tick(120)  
