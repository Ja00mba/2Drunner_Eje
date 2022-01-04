def check_collision(self, pipes):
    for pipe in pipes:
        if self.character_rect.colliderect(pipe):
            return False
    if self.character_rect.top <= -100 or self.character_rect.bottom >= 596:
        return False
    return True


def create_obstacle(self):
    random_pipe_pos = random.randint(200, 520)

    bottom_pipe = self.pipe_surface.get_rect(midtop=(1350, random_pipe_pos))
    top_pipe = self.pipe_surface.get_rect(midbottom=(1350, random_pipe_pos - 150))
    return bottom_pipe, top_pipe


def move_obstacle(self, pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_obstacle(self, pipes, screen):
    for pipe in pipes:
        if pipe.bottom >= 596:
            screen.blit(self.pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
