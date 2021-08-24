import pygame, sys, time
from snake import Snake
from score import Score
from food import Food

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Screen parameters
width = 400
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Player
player = Snake(width, height)
scoreboard = Score()
food = Food()

# Timer
time_left = 300

# Game Sound
snake_eat_sound = pygame.mixer.Sound("snakehit.wav")
special_sound = pygame.mixer.Sound("special.mp3")

def game():
    global time_left
    running = True
    while running:
        screen.fill((57, 255, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if not player.move_down:
                        player.move_up = True
                        player.move_right = False
                        player.move_left = False
                        player.move_down = False

                if event.key == pygame.K_s:
                    if not player.move_up:
                        player.move_down = True
                        player.move_right = False
                        player.move_left = False
                        player.move_up = False

                if event.key == pygame.K_d:
                    if not player.move_left:
                        player.move_right = True
                        player.move_up = False
                        player.move_down = False
                        player.move_left = False

                if event.key == pygame.K_a:
                    if not player.move_right:
                        player.move_left = True
                        player.move_up = False
                        player.move_down = False
                        player.move_right = False

        scoreboard.show_score(screen)

        # Collision with food:
        if player.collide_point(food.foods[0]):
            pygame.mixer.Sound.play(snake_eat_sound)
            player.add_body(food.foods[0].x, food.foods[0].y)
            food.remove()
            if scoreboard.recorder % 10 == 0 and scoreboard.recorder != 0:
                scoreboard.add_score(False)
            else:
                scoreboard.add_score(True)

        pygame.draw.rect(screen, (0, 0, 0), (10, 20, 380, 370))
        pygame.draw.ellipse(screen, (255, 49, 49), food.foods[0])

        if scoreboard.recorder % 10 == 0 and scoreboard.recorder != 0:
            pygame.mixer.Sound.play(special_sound)
            time_left -= 1
            if time_left > 0:
                pygame.draw.ellipse(screen, (255, 49, 49), food.special_foods[0])
                if player.collide_point(food.special_foods[0]):
                    food.remove_special()
                    scoreboard.score += 5
                    scoreboard.reset_record()
                    time_left = 300
            else:
                food.remove_special()
                scoreboard.reset_record()
                time_left = 300

        player.move_head()
        player.move_body()
        for x in player.body:
            pygame.draw.rect(screen, (57, 255, 20), x)

        if len(player.body) >= 1:
            for x in range(10, len(player.body)):
                if player.collide_point(player.body[x]):
                    running = False

        pygame.display.flip()

        clock.tick(60)

    scoreboard.show_lose(screen)
    pygame.display.update()
    time.sleep(3)

if __name__ == '__main__':
    game()