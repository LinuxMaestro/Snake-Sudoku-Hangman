"""
A LOT OF CODE FROM THIS PROGRAM CAME FROM A YOUTUBE CHANNEL TECH WITH TIM
I added quite some tweaks to it

FOUND THE BACKGROUND MUSIC AT http://dig.ccmixter.org/games
FORGOTTENLAND By airtone
FOUND THE SOUND EFFECT AT http://soundbible.com/1394-Dragon-Bite.html
DRAGONBITE by GregoryWeir

NOT EDITED
NOT FOR PROFIT, SOLELY FOR EDUCATIONAL PURPOSES
"""

from pygame import *
import random, sys
import os
from pathlib import Path

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WH = (SCREEN_WIDTH, SCREEN_HEIGHT)
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1),  (-1, 0), (1, 0)
DIRECTION_BOX = [UP, DOWN, LEFT, RIGHT]
GAME_DIRECTION = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
GRID = 20
GRID_BOX = (GRID, GRID)
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH//GRID, SCREEN_HEIGHT//GRID

BG_IMG = os.path.join(Path.cwd(), "photo-1552820728-8b83bb6b773f.jpg")
BGM_At = os.path.join(Path.cwd(), "airtone_-_forgottenland.wav")
SOUND_At = os.path.join(Path.cwd(), "Dragon Bite-SoundBible.com-1625781385.wav")
print(BGM_At, SOUND_At)
def actual_background(surface):
    img = image.load(BG_IMG)
    surface.blit(img, (0, 0))
    display.flip()
class cube:
    def __init__(self):
        self.position = (3,2)
        self.color = (223,163,49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID, random.randint(0, GRID_HEIGHT-1) * GRID)

    def draw(self, surface):
        box = Rect((self.position[0], self.position[1]), GRID_BOX)
        draw.rect(surface, self.color, box)
        draw.rect(surface, (93,216,228), box, 1)

class Snake:
    def __init__(self):
        self.length = 1
        self.body = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]
        self.direction = random.choice(DIRECTION_BOX)
        self.color = (0,255,255) # CYAN
        self.score = 0

    def head_at(self):
        return self.body[0]

    def turn(self, toward):
        if self.length > 1 and (-toward[0], -toward[1]) == self.direction:
            return
        else:
            self.direction = toward

    def move(self):
        head = self.head_at()
        x, y = self.direction
        new = (((head[0]+(x*GRID))%SCREEN_WIDTH), (head[1]+(y*GRID))%SCREEN_HEIGHT)
        if len(self.body) > 2 and new in self.body[2:]:
            self.reset()
        else:
            self.body.insert(0, new)
            if len(self.body) > self.length:
                self.body.pop()

    def reset(self):
        self.length = 1
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice(DIRECTION_BOX)
        self.score = 0


    def draw(self, surface):
        for part in self.body:
            box = Rect(part, GRID_BOX)
            draw.rect(surface, self.color, box)
            draw.rect(surface, (93,216,228), box, 1)

    def handle_inputs(self):
        for i in event.get():
            if i.type == QUIT:
                quit()
                exit()
            elif i.type == KEYDOWN:
                if i.key in GAME_DIRECTION:
                    j = GAME_DIRECTION.index(i.key)
                    self.turn(DIRECTION_BOX[j])

def draw_bg_grid(surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            box = Rect((x * GRID, y * GRID), GRID_BOX)
            if (x + y) % 2 == 0:
                draw.rect(surface, (93, 216, 228), box)
            else:
                draw.rect(surface, (84, 194, 205), box)


if __name__ == "__main__":
    init()
    display.set_caption("채연이는 1년뒤 청소년, 15살!!")

    clock = time.Clock()
    screen = display.set_mode(SCREEN_WH, 0, 32)

    surface = Surface(screen.get_size())
    surface = surface.convert()
    draw_bg_grid(surface)
    # actual_background(surface)
    snake = Snake()
    food = cube()

    game_font = font.SysFont("monospace", 16)
    mixer.init()
    BGM_MUSIC = mixer.Sound(BGM_At)
    BGM_MUSIC.play()

    while True:
        clock.tick(10)
        snake.handle_inputs()
        # draw_bg_grid(surface)
        actual_background(surface)
        snake.move()
        if snake.head_at() == food.position:
            SOUND_EFFECT = mixer.Sound(SOUND_At)
            SOUND_EFFECT.play()
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = game_font.render(f"Score is {snake.score}", 1, (255,255,255))
        screen.blit(text, (5, 10))
        display.update()

