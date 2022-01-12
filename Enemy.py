import pygame


class Opponent:
    def __init__(self):
        self.WoodCutterEnemySurface = pygame.image.load('assets/sprites/character_anim/EnemyIdle/Woodcutter.png')

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

    def get_surface(self):
        return self.WoodCutterEnemySurface

    def get_attack(self):
        return self.WoodCutterEnemyBeatAnimation

    def get_death(self):
        return self.WoodCutterEnemyDeathAnimation

    def get_frame(self, attack):
        if attack:
            return self.WoodCutterEnemyBeatAnimation
        return [self.WoodCutterEnemySurface for _ in range(6)]
