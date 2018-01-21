#! /usr/bin/env python3
# coding: utf-8

""" imports all necessary modules, get all paths to images,
set default size image and start/end positions
and launch the game : main() """

# pylint: disable=no-name-in-module

# import from standard modules
from os.path import dirname as path_dirname
from random import choice
from time import sleep
# import from third party module : pygame
from pygame import init as pg_init
from pygame.display import set_mode as pg_set_mode
from pygame.key import set_repeat as pg_set_repeat
from pygame.display import flip as pg_flip
from pygame.image import load as pg_load
from pygame.event import get as pg_get
from pygame.font import SysFont as pg_SysFont
from pygame.locals import QUIT, KEYDOWN
# import from local modules
from library.background.background import Background
from library.element.element import Element
from library.play_game.play_game import play_game

# find the path to default_map.txt, and all images for :
# background
# all elements : biscotte, cheese, end_img
MAIN_DIR = path_dirname(__file__)
PATH_TO_MAP = MAIN_DIR + "/maps/default_map.txt"
PATH_TO_WALL = MAIN_DIR + "/img/wall.png"
PATH_TO_FLOOR = MAIN_DIR + "/img/floor.png"
PATH_TO_BISCOTTE = MAIN_DIR + "/img/biscotte.png"
PATH_TO_CHEESE = MAIN_DIR + "/img/cheese.png"
PATH_TO_END_IMG = MAIN_DIR + "/img/end.png"

# set the size of image, start and end points
SIZE_IMG = (45, 45)
START_POINT = (45, 45)


def main():
    """ create all the variables before run the gui
    and play the game with module pygame"""

    # !! create all the variables necessary for the game !!
    # create the labyrinth, biscotte with default positions
    labyrinth = Background(
        PATH_TO_MAP, PATH_TO_WALL, PATH_TO_FLOOR, SIZE_IMG)
    biscotte = Element(PATH_TO_BISCOTTE, START_POINT, "player", SIZE_IMG)
    # remove the positions of biscotte in avalaible positions
    labyrinth.available_positions.remove(biscotte.position)
    # random choice for position and create the cheese
    cheese = Element(
        PATH_TO_CHEESE, choice(labyrinth.available_positions),
        "recoverable", SIZE_IMG)
    # create the end image that appear in counter when 10 cheeses are founded
    end_img = Element(PATH_TO_END_IMG, (
        (labyrinth.size_window[0] - SIZE_IMG[0]), (
            labyrinth.size_window[1] - SIZE_IMG[1])), "", SIZE_IMG)
    # create a list of game's elements
    game_elements = [biscotte, cheese, end_img]
    # initialise available positions of the labyrinth
    labyrinth.__init__(PATH_TO_MAP, PATH_TO_WALL, PATH_TO_FLOOR, SIZE_IMG)

    # !! create the gui !!
    # create a window
    pg_init()
    window = pg_set_mode(labyrinth.size_window)
    # set moving when the key reaims depressed
    pg_set_repeat(400, 30)
    # create object Surface for each zone of background
    for key in labyrinth:
        labyrinth[key] = pg_load(labyrinth[key]).convert_alpha()
    # create object Surface for each element
    for element in game_elements:
        element.img = pg_load(element.img).convert_alpha()
    # create an object Rect for the player
    biscotte_rect = biscotte.img.get_rect(topleft=START_POINT)

    # !! play the game !!
    # initialize the counter and the list of elements:
    counter_elts_founded = 0
    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pg_get():
            if event.type == QUIT:  # if window is closed
                gui_display = 0
            elif event.type == KEYDOWN:  # if the keyboard is used
                biscotte, biscotte_rect, cheese, counter_elts_founded = play_game(
                    event, biscotte, biscotte_rect, cheese, counter_elts_founded,
                    labyrinth)
        # paste all on the window
        # background
        for key in labyrinth:
            window.blit(labyrinth[key], key)
        # game's elements
        if counter_elts_founded != 5:
            window.blit(cheese.img, cheese.position)
        else:
            window.blit(end_img.img, (200, labyrinth.counter_position[1]))
            window.blit(pg_SysFont('Comic Sans MS', 35).render("Merci", False, (
                120, 9, 9)), ((SIZE_IMG[0] * 2), labyrinth.counter_position[1]))
        # counter
        window.blit(cheese.img, labyrinth.counter_position)
        window.blit(pg_SysFont('Comic Sans MS', 35).render(
            str(counter_elts_founded), False, (75, 9, 9)), ((int((
                SIZE_IMG[0] / 10))), labyrinth.counter_position[1]))
        # player
        window.blit(biscotte.img, biscotte_rect)
        # refresh window
        pg_flip()
        # verify if the end
        if counter_elts_founded == 5:
            # close window if player finish the game
            gui_display = 0
            sleep(2.5)


if __name__ == "__main__":
    main()
