
import pygame

class Paddle:
    def __init__(self, window_size, color, start_x, start_y, width, height, vel, key_up, key_down):
        self.w_widht, self.w_height = window_size
        self.color = color
        self.x = self.x_origin = start_x
        self.y = self.y_origin = start_y 
        self.width = width
        self.height = height
        self.vel = vel
        self.key_up = key_up
        self.key_down = key_down
    
    def move(self):
        key_input = pygame.key.get_pressed()
        if key_input[self.key_up] and self.y >= 0:
            self.y -= self.vel
        if key_input[self.key_down] and self.y+self.height <= self.w_height:
            self.y += self.vel

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.x = self.x_origin
        self.y = self.y_origin

class Ball:
    def __init__(self, color, size, start_x, start_y, vel_x, vel_y):
        self.color = color
        self.size = size
        self.x = self.x_origin = start_x-self.size/2
        self.y = self.y_origin = start_y-self.size/2
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    
    def reset(self, direction, vel):
        self.x = self.x_origin
        self.y = self.y_origin
        self.vel_y = 0
        self.vel_x = direction/abs(direction) * vel


class FieldLines:
    def __init__(self, color, position, thickness):
        self.color = color
        self.position = position
        self.thickness = thickness

    def draw_h_line(self, window, height):
        for i in range(0, height, int(height/20)+1):
            pygame.draw.rect(window, self.color, (self.position-self.thickness/2, i, self.thickness, int(height/40)))
