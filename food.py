import pygame, random


class Food:

    def __init__(self):
        self.foods = [pygame.Rect(random.randint(20, 380), random.randint(20, 365), 8, 8)]
        self.special_foods = [pygame.Rect(random.randint(20, 380), random.randint(20, 365), 12, 12)]
        self.specials_eaten = 0

    def create_food(self):
        food = pygame.Rect(random.randint(20, 380), random.randint(20, 365), 8, 8)
        self.foods.append(food)

    def remove(self):
        self.foods.pop()
        self.create_food()

    def special(self):
        special = pygame.Rect(random.randint(20, 380), random.randint(20, 365), 12, 12)
        self.special_foods.append(special)

    def remove_special(self):
        self.specials_eaten += 1
        self.special_foods.pop()
        self.special()

