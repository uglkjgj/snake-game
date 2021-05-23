import pygame

class Score:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 15)
        self.recorder = 0

    def show_score(self, screen):
        player_text = self.font.render(f"{self.score}", False, (0, 0, 0))
        screen.blit(player_text, (370, 3))

    def add_score(self, yes):
        if yes:
            self.score += 1
            self.recorder += 1
        else:
            self.score += 1

    def reset_record(self):
        self.recorder = 0

    def show_lose(self, screen):
        player_text = self.font.render(f"You Lose", False, (255, 255, 255))
        screen.blit(player_text, (180, 200))
