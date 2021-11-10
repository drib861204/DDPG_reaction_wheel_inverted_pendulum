"""
Title: pendulum_pygame
Author: [jadenhensley](https://github.com/jadenhensley)
Last modified: 2021/10/18
Description: Pendulum project, built using pygame and math modules.

Title: wheelPole
Author: [aimetz](https://github.com/aimetz)
Last modified: 2021/04/20
"""
import pygame
from math import pi, sin, cos, floor


class Pendulum:
    #height = 600
    #width = 800
    #gravity = 0.01

    #win = pygame.display.set_mode((width, height))
    #pygame.display.set_caption("Pendulum Simulation")

    #objects_group = []

    #pygame.font.init()

    #debug_font = pygame.font.SysFont('Bauhuas 93', 30)
    #hint_font = pygame.font.SysFont('Bauhaus 93', 26)

    def __init__(self):
        self.theta_rod = 0
        self.theta_wheel = 0
        self.len_rod = 100
        self.len_wheel = 200
        self.mass_rod = 10
        self.mass_wheel = 50
        self.momentum_rod = 5
        self.momentum_wheel = 10

        height = 600
        width = 800
        gravity = 0.01
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pendulum Simulation")
        pygame.init()

        '''
        self.ball_x = 20
        self.ball_y = 20
        self.orn_x = width//2
        self.orn_y = height//2
        self.radius = 15
        self.color = (224, 36, 1)
        #self.origin = Origin(width // 2, self.y)
        self.angle = pi / 4
        self.angle_velocity = .1
        self.angle_acceleration = 0
        self.len = 200
        self.timer = 0
        '''

    def reset(self):
        self.theta_rod = pi/18
        self.theta_wheel = 0
        state = [theta_rod, theta_wheel]
        return state


    #def render(self):



    def step(self, action):
        torque = action
        eff_momentum_1 = self.mass_rod*self.len_rod**2+self.mass_wheel*self.len_wheel**2+self.momentum_rod+self.momentum_wheel
        eff_momentum_2 = self.momentum_wheel
        #state =





    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        win.blit(img, (x, y))


    def draw(self):
        # global gravity
        force = gravity * sin(self.angle)
        self.angle_acceleration = (-1 * force) / self.len
        self.angle_velocity += self.angle_acceleration
        self.angle += self.angle_velocity

        self.x = self.len * sin(self.angle) + self.origin.x
        self.y = self.len * cos(self.angle) + self.origin.y

        self.origin.draw()
        pygame.draw.line(win, (216, 233, 168), (self.origin.x, self.origin.y), (self.x, self.y))
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

        self.timer += 1

        draw_text(f"Current gravity: {gravity}", debug_font, (255, 255, 255), width // 2, 30)
        draw_text(f"Current acceleration: {self.angle_acceleration}", debug_font, (255, 255, 255), width // 2, 60)
        draw_text(f"Current momentum: {self.angle_velocity}", debug_font, (255, 255, 255), width // 2, 90)
        draw_text(f"Press up or down key to change length! ", hint_font, (255, 255, 255), 10, 30)
        draw_text(f"Current length: {self.len} ", hint_font, (255, 255, 255), 10, 60)

        if self.timer > 40:
            if gravity <= 160:
                if gravity >= 10:
                    gravity += 2
                    gravity = floor(gravity)
                else:
                    if gravity >= 1:
                        gravity += 1
                        gravity = floor(gravity)
                    else:
                        gravity += .10
            self.timer = 0

    '''
    def Origin(self, x, y, color=(216, 233, 168)):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = color
        
    def draw_origin(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    '''


def update(window, obj_group):
    win.fill((25, 26, 25))
    for obj in obj_group:
        obj.draw()
    pygame.display.update()

def main():
    global gravity
    run = True
    clock = pygame.time.Clock()

    # p_origin = Origin(width // 2, height // 2 - 200)
    pendulum = Pendulum(20, height // 2 - 200, 450)
    # objects_group.append(p_origin)
    objects_group.append(pendulum)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                run = False
                pygame.quit()
            if key[pygame.K_UP]:
                pendulum.len -= 10
            if key[pygame.K_DOWN]:
                pendulum.len += 10
            if key[pygame.K_r]:
                # reset pendulum position, physics
                pendulum.angle_velocity = .1
                pendulum.angle_acceleration = 0
                pendulum.angle = pi / 4
                pendulum.timer = 0
                gravity = .01

        update(win, objects_group)

# main()