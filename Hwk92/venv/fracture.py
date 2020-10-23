import pygame, math
from pygame_button import Button

# colors fromm button example
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)
PURPLE = (128, 0, 128)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

RUNNING, PAUSE = 0, 1

pygame.init()  # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size, surface_size))
my_clock = pygame.time.Clock()


def color_of_depth(d):
    switcher = {
        0: RED,
        1: GREEN,
        2: BLUE,
        3: BLACK,
        4: WHITE,
        5: ORANGE,
        6: PURPLE,
        7: MAGENTA,
        8: CYAN
    }

    return switcher.get(d, "Invalid color ")


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

        # change color when even/odd

        color = color_of_depth(depth)

        # make the recursive calls to draw the two subtrees
        newsz = sz * (1 - trunk_ratio)
        draw_tree(order - 1, theta, newsz, newpos, heading - theta, color, depth + 1)
        draw_tree(order - 1, theta, newsz, newpos, heading + theta, color, depth + 1)


def gameloop():
    theta = 0
    while not done:

        # Handle evente from keyboard, mouse, etc.
        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        quit_btn.check_event(ev)
        pause_btn.check_event(ev)

        if state == RUNNING:
            '''Draw the tree'''
            # Updates - change the angle
            theta += 0.01

            # Draw everything
            main_surface.fill((255, 255, 0))
            draw_tree(9, theta, surface_size * 0.9, (surface_size // 2, surface_size - 50), -math.pi / 2)

        elif state == PAUSE:
            """Draw the pause screen"""
            # put text to screen
            pygame.font.init()
            bigfont = pygame.font.SysFont('Comic Sans MS', 90)
            textsurface = bigfont.render('Paused', False, (0, 0, 0))

            # center the text on the screen
            main_surface.blit(textsurface, ((surface_size // 2) - textsurface.get_width() // 2, surface_size // 2))

            littlefont = pygame.font.SysFont('Comic Sans MS', 25)
            textsurface = littlefont.render('Press Quit to Quit, Press Play/Pause to Continue.', False, (0, 0, 0))

            # center the text on the screen
            main_surface.blit(
                textsurface,
                (
                (surface_size // 2) - textsurface.get_width() // 2, (surface_size // 2) + textsurface.get_height() * 4))

        quit_btn.update(main_surface)  # add the quit button to the surface
        pause_btn.update(main_surface)  # add the pause button to the surface
        pygame.display.flip()           # show the surface
        my_clock.tick(120)
        continue

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

state = RUNNING

def pause():
    global state
    #toggle RUNNING nad PAUSE
    #This merely switches the state
    state = RUNNING if state == PAUSE else PAUSE


quit_btn = Button((0, 0, 200, 50), RED, end, text='Quit', **BUTTON_STYLE)
pause_btn = Button((200, 0, 200, 50), RED, pause, text='Play/Pause', **BUTTON_STYLE)

gameloop()
pygame.quit()
