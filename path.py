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

# Creating a Node class 
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row, 
        self.col = col, 
        self.x = row * width, 
        self.y = col * width, 
        self.width = width
        self.color = WHITE,
        self.neighbors = [], 
        self.total_rows = total_rows
        
    def get_position(self):
        return self.row, self.col
    
    
    # Specify if a node has been checked 
    def is_closed(self):
        return self.color == RED
    
    # Specify if a node is open
    def is_open(self):
        return self.color == GREEN
    
    # Specify if a node is a barrier
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == BLUE
    
    def reset(self):
        return self.color == WHITE
    
    
    # Functions that are creating nodes
    
    def make_closed(self):
        self.color = RED
        
    def make_open(self):
        self.color = GREEN
        
    def make_barrier(self):
        self.color = BLACK
        
    def make_end(self):
        self.color = BLUE
        
    def make_path(self):
        self.color = PURPLE
        
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbors(self, grid):
        pass
    
    # Less than function
    def __lt__(self, other):
        return False
    
# Heuristic function
def heuristics(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)