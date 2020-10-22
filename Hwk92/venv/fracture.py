import pygame, math
from pygame_button import Button

pygame.init()  # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, sz, posn, heading, color=(0, 0, 0), depth=0):
    trunk_ratio = 0.29  # How big is the trunk relative to whole tree?
    trunk = sz * trunk_ratio  # length of trunk
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = posn
    newpos = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, posn, newpos)

    if order > 0:  # Draw another layer of subtrees

        # These next six lines are a simple hack to make the two major halves
        # of the recursion different colors. Fiddle here to change colors
        # at other depths, or when depth is even, or odd, etc.
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

        # make the recursive calls to draw the two subtrees
        newsz = sz * (1 - trunk_ratio)
        draw_tree(order - 1, theta, newsz, newpos, heading - theta, color1, depth + 1)
        draw_tree(order - 1, theta, newsz, newpos, heading + theta, color2, depth + 1)


def gameloop():
    theta = 0
    while not done:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        button.check_event(ev)

        # Updates - change the angle
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size * 0.9, (surface_size // 2, surface_size - 50), -math.pi / 2)

        button.update(main_surface) #add the button to the surface

        pygame.display.flip()
        my_clock.tick(120)


# colors fromm button example
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

# The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {
    "hover_color": BLUE,
    "clicked_color": GREEN,
    "clicked_font_color": BLACK,
    "hover_font_color": ORANGE,
    "hover_sound": None,
}

done = False


def end():
    global done
    done = True


button = Button((0, 0, 200, 50), RED, end, text='Quit', **BUTTON_STYLE)

gameloop()
pygame.quit()
