import pygame, sys, random


class logic():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.floor_x_pos = 0
        self.bird_movement = 0
        self.pipe_list = []
        self.pipe_height = (200, 520)

        pipe_surface = pygame.image.load('assets/sprites/pipe-green.png')
        self.pipe_surface = pygame.transform.scale(pipe_surface, (65, 400))

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1200)

        self.bird_surface = pygame.image.load('assets/sprites/subeerow.png')

        self.bird_rect = self.bird_surface.get_rect(center=(100, 360))

    def create_pipe(self):
        random_pipe_pos = random.randint(200, 520)

        bottom_pipe = self.pipe_surface.get_rect(midtop=(1350, random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(1350, random_pipe_pos - 150))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(self, pipes, screen):
        for pipe in pipes:
            if pipe.bottom >= 596:
                screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def draw_bg(self, screen):
        bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()
        screen.blit(bg_surface, (0, 0))

    def draw_floor(self, screen):
        floor_surface = pygame.image.load('assets/sprites/base.png').convert()
        floor_surface = pygame.transform.scale2x(floor_surface)

        self.floor_x_pos -= 1
        screen.blit(floor_surface, (self.floor_x_pos, 596))
        screen.blit(floor_surface, (self.floor_x_pos + 1280, 596))
        screen.blit(self.bird_surface, self.bird_rect)

    def check_collision(self, pipes):
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                return False
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 596:
            return False
        return True


if __name__ == '__main__':
    pygame.init()
    FPS = 60
    SIZE = WIDTH, HEIGHT = 1280, 720

    running = True
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    game = logic(WIDTH, HEIGHT)
    GRAVITY = 1.5
    game_active = True
    game.bird_movement = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    game.bird_movement = 0
                    game.bird_movement -= 16
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    game.pipe_list.clear()
                    game.bird_rect.center = (100, 360)
                    game.bird_movement = 0
                    game.bird_movement -= 16
            if event.type == game.SPAWNPIPE:
                game.pipe_list.extend(game.create_pipe())

        game.draw_bg(screen)

        if game_active:
            game_active = game.check_collision(game.pipe_list)
            game.bird_movement += GRAVITY
            game.bird_rect.centery += game.bird_movement
            game.pipe_list = game.move_pipes(game.pipe_list)
            game.draw_pipes(game.pipe_list, screen)

        game.draw_floor(screen)

        if game.floor_x_pos <= -576:
            game.floor_x_pos = 0
        pygame.display.update()
        clock.tick(120)
