# A* Pathfinding Algorithm Visualizer using PyGame

import pygame
import math
from queue import PriorityQueue

# Setting the windows dimensions
WIDTH = 800
HEIGHT = 800

# Inizializing the main window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding Algorithm Visualizer")

# Defining basic colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
