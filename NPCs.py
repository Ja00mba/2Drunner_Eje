class Enemy:
    def __init__(self, ShootAnim, IdlePic, DeathAnim, animCount):
        self.ShootAnim = ShootAnim
        self.IdlePic = IdlePic
        self.DeathAnim = DeathAnim
        self.animCount = animCount

    def Spawn(self, screen, coords):
        screen.blit(self.IdlePic, coords)

    def Attack(self, screen, coords):
        if self.animCount >= 15:
            self.animCount = 0
        screen.blit(self.ShootAnim[self.animCount // 5], coords)
        self.animCount += 1
