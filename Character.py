import pygame


class Character:
    def __init__(self):
        self.step = 0

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

    def get_surface(self):
        pass

    def get_run(self):
        return self.runAnimation

    def get_attack(self):
        return self.BeatAnimation

    def get_frame(self, attack):
        if attack:
            return self.BeatAnimation
        return self.runAnimation

