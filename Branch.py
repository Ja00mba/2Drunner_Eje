import pygame
import sys
import random
from Enemy import Opponent
from Character import Character

pygame.init()


class logic():
    floor_surface = pygame.image.load('assets/sprites/Background/City4.png')

    road_surface = pygame.image.load('assets/sprites/Background/road.png')

    obstacles = [pygame.image.load('assets/sprites/Obstacles/Trash2.png'),
                 pygame.image.load('assets/sprites/Obstacles/boxes2.png'),
                 pygame.image.load('assets/sprites/Obstacles/minishop2.png'),
                 pygame.image.load('assets/sprites/Obstacles/wheels2.png'),
                 ]

    def __init__(self, screen):

        self.floor_surface = logic.floor_surface
        self.road_surface = logic.road_surface
        self.obstacles = logic.obstacles

        self.anim_frames = []
        self.enemy_frames = []

        self.screen = screen
        self.bg_pos = 0
        self.road_pos = 0
        self.obstaclePos = 0
        self.obstacle_index = 0
        self.Beat = False
        self.enemy_count = 0
        self.EnemyPos = 1280

        self.animCount = 0

    #        self.EnemyRect = self.Enemy_surface.get_rect(center=(self.EnemyPos, 550))

    def animate_enemy(self):
        self.EnemyPos -= 8
        if self.enemy_count == 0:
            self.enemy_frames.clear()
            self.enemy_frames = [i for i in Opponent().get_frame(False)]
        if self.enemy_count >= 24:
            self.enemy_frames.clear()
            self.enemy_frames = [i for i in Opponent().get_frame(False)]
            self.enemy_count = 0
        self.screen.blit(self.enemy_frames[self.enemy_count // 4], (self.EnemyPos, 550))
        self.enemy_count += 1

    def DrawObstacles(self):
        if self.obstaclePos == 0:
            self.obstacle_index = random.randint(0, len(self.obstacles) - 1)
        self.obstaclePos -= 8
        self.screen.blit(self.obstacles[self.obstacle_index], (self.obstaclePos + 1280, 450))
        self.screen.blit(self.obstacles[self.obstacle_index - 1], (self.obstaclePos + 1616, 450))

    def animate_character(self):
        if self.animCount == 0:
            self.anim_frames.clear()
            self.anim_frames = [i for i in Character().get_frame(self.Beat)]

        if self.animCount >= 24:
            self.anim_frames.clear()
            self.anim_frames = [i for i in Character().get_frame(self.Beat)]
            self.animCount = 0
            self.Beat = False

        self.screen.blit(self.anim_frames[self.animCount // 4], (100, 570))
        self.animCount += 1

    def DrawFloor(self):
        self.bg_pos -= 5
        self.screen.blit(self.floor_surface, (self.bg_pos, 0))
        self.screen.blit(self.floor_surface, (self.bg_pos + 1280, 0))

    def DrawRoad(self):
        self.road_pos -= 8
        self.screen.blit(self.road_surface, (self.road_pos, 0))
        self.screen.blit(self.road_surface, (self.road_pos + 1280, 0))


if __name__ == '__main__':

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.Beat = True

        game.DrawFloor()
        game.DrawRoad()
        game.DrawObstacles()
        game.animate_enemy()
        game.animate_character()

        if game.EnemyPos <= -144:
            game.EnemyPos = 1280
        if game.bg_pos <= -1280:
            game.bg_pos = 0
        if game.road_pos <= -1280:
            game.road_pos = 0
        if game.obstaclePos <= -1952:
            game.obstaclePos = 0
        pygame.display.update()
        clock.tick(FPS)
