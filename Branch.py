import pygame
import sys
import random


class logic():
    def __init__(self, screen):
        self.screen = screen
        self.bg_pos = 0
        self.road_pos = 0
        self.obstaclePos = 0
        self.obstacle_index = 0

        self.animCount = 0

        self.floor_surface = pygame.image.load('assets/sprites/Background/City4.png').convert()
        self.road_surface = pygame.image.load('assets/sprites/Background/road.png')

        self.runAnimation = [pygame.image.load('assets/sprites/character_anim/RunAnim_1.png'),
                             pygame.image.load('assets/sprites/character_anim/RunAnim_2.png'),
                             pygame.image.load('assets/sprites/character_anim/RunAnim_3.png'),
                             pygame.image.load('assets/sprites/character_anim/RunAnim_4.png'),
                             pygame.image.load('assets/sprites/character_anim/RunAnim_5.png'),
                             pygame.image.load('assets/sprites/character_anim/RunAnim_6.png')]

        self.obstacles = [pygame.image.load('assets/sprites/Obstacles/Trash2.png'),
                          pygame.image.load('assets/sprites/Obstacles/boxes2.png'),
                          pygame.image.load('assets/sprites/Obstacles/minishop2.png'),
                          pygame.image.load('assets/sprites/Obstacles/wheels2.png'),
                          ]

    def DrawObstacles(self):
        if self.obstaclePos == 0:
            self.obstacle_index = random.randint(0, len(self.obstacles) - 1)
        self.obstaclePos -= 15
        self.screen.blit(self.obstacles[self.obstacle_index], (self.obstaclePos + 1280, 450))
        self.screen.blit(self.obstacles[self.obstacle_index - 1], (self.obstaclePos + 1616, 450))

    def DrawCharacter(self):
        if self.animCount >= 15:
            self.animCount = 0
        self.screen.blit(self.runAnimation[self.animCount // 5], (100, 570))
        self.animCount += 1

    def DrawFloor(self):
        self.bg_pos -= 5
        self.screen.blit(self.floor_surface, (self.bg_pos, 0))
        self.screen.blit(self.floor_surface, (self.bg_pos + 1280, 0))

    def DrawRoad(self):
        self.road_pos -= 15
        self.screen.blit(self.road_surface, (self.road_pos, 0))
        self.screen.blit(self.road_surface, (self.road_pos + 1280, 0))


if __name__ == '__main__':
    pygame.init()
    FPS = 60
    SIZE = WIDTH, HEIGHT = 1280, 720

    running = True
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    game = logic(screen)
    GRAVITY = 1.5
    game_active = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.DrawFloor()

        game.DrawRoad()
        game.DrawObstacles()
        game.DrawCharacter()

        if game.bg_pos <= -1280:
            game.bg_pos = 0
        if game.road_pos <= -1280:
            game.road_pos = 0
        if game.obstaclePos <= -1952:
            game.obstaclePos = 0
        pygame.display.update()
        clock.tick(FPS)
