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
        self.Beat = False
        self.Attack_animCount = 0
        self.AttackCount = 0
        self.EnemyPos = 1280

        self.animCount = 0

        self.WoodCutterEnemySurface = pygame.image.load('assets/sprites/character_anim/EnemyIdle/Woodcutter.png')
        self.EnemyRect = self.WoodCutterEnemySurface.get_rect(center=(self.EnemyPos, 550))

        self.WoodCutterEnemyBeatAnimation = [
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_1.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_2.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_3.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_4.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_5.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyAttack/WoodCutterAttac_6.png')]

        self.WoodCutterEnemyDeathAnimation = [
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_1.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_2.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_3.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_4.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_5.png'),
            pygame.image.load('assets/sprites/character_anim/EnemyDeath/new_type/WoodCutterDeath_6.png')]

        self.floor_surface = pygame.image.load('assets/sprites/Background/City4.png').convert()

        self.road_surface = pygame.image.load('assets/sprites/Background/road.png')

        self.BeatAnimation = [pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_1.png'),
                              pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_2.png'),
                              pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_3.png'),
                              pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_4.png'),
                              pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_5.png'),
                              pygame.image.load('assets/sprites/character_anim/Beat/BeatAnim_6.png')]

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

    def spawnEnemy(self):
        self.EnemyPos -= 8
        self.screen.blit(self.WoodCutterEnemySurface, (self.EnemyPos, 550))
        return self.WoodCutterEnemySurface.get_rect()

    def DeathEnemy(self):
        self.EnemyPos -= 8
        if self.Attack_animCount >= 30:
            self.Attack_animCount = 0
        self.screen.blit(self.WoodCutterEnemyDeathAnimation[self.Attack_animCount // 5], (self.EnemyPos, 550))
        self.Attack_animCount += 1

    def AttackEnemy(self):
        self.EnemyPos -= 8
        if self.Attack_animCount >= 30:
            self.Attack_animCount = 0
        self.screen.blit(self.WoodCutterEnemyBeatAnimation[self.Attack_animCount // 5], (self.EnemyPos, 550))
        self.Attack_animCount += 1

    def DrawObstacles(self):
        if self.obstaclePos == 0:
            self.obstacle_index = random.randint(0, len(self.obstacles) - 1)
        self.obstaclePos -= 8
        self.screen.blit(self.obstacles[self.obstacle_index], (self.obstaclePos + 1280, 450))
        self.screen.blit(self.obstacles[self.obstacle_index - 1], (self.obstaclePos + 1616, 450))

    def DrawAttack(self):
        if self.AttackCount >= 30:
            self.AttackCount = 0
            self.Beat = False
        self.screen.blit(self.BeatAnimation[self.AttackCount // 5], (100, 570))
        self.AttackCount += 1

    def DrawCharacter(self):
        if self.animCount >= 30:
            self.animCount = 0
        self.screen.blit(self.runAnimation[self.animCount // 5], (100, 570))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game.Beat:
                        game.Beat = True
                    else:
                        pass

        game.DrawFloor()
        game.DrawRoad()
        game.DrawObstacles()
        if game.Beat:
            game.DrawAttack()
            game.DeathEnemy()

        else:
            game.spawnEnemy()
            game.DrawCharacter()
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
