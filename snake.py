import pygame


class Snake:

    def __init__(self, screen_width, screen_height):
        self.head = pygame.Rect(screen_width/2 - 5, screen_height/2 - 5, 10, 10)
        self.body = [self.head]
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def add_body(self, x, y):
        self.body.append(pygame.Rect(x+10, y+10, 10, 10))

    def move_head(self):
        if self.move_up:
            self.body[0].y -= 2
        elif self.move_down:
            self.body[0].y += 2
        elif self.move_right:
            self.body[0].x += 2
        elif self.move_left:
            self.body[0].x -= 2

        if self.head.y >= 390:
            self.body[0].y = 10
        elif self.head.y <= 10:
            self.body[0].y = 390
        elif self.head.x >= 390:
            self.body[0].x = 10
        elif self.head.x <= 10:
            self.body[0].x = 390

    def move_body(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].center = self.body[i-1].center

    def collide_point(self, rect):
        if self.body[0].colliderect(rect):
            return True

