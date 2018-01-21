#! /usr/bin/env python3
# coding: utf-8

""" Module with function play_game
configuring to use with module pygame.locals"""

# pylint: disable=no-name-in-module
# pylint: disable=too-many-arguments

# import from standard modules
from random import choice
# import from third party module : pygame.locals
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN


def play_game(
        event, player, player_rect, element, counter_elts_founded,
        background):
    """find the direction, move the player if necessary,
    found element if there is one at the new position,
    check if the player win or lose
    before return all with update.
    event : event from pygame with type KEYDOWN
    player : class Element
    player_rect : class Rect
    element : objects with class Element
    counter_elts_founded : int
    background : class Background"""
    # initialise movement
    movement = 0
    # find the direction ...
    if event.key == K_LEFT:
        # ... and test the movement
        movement = player.check_movement(
            background.available_positions, "left")
    elif event.key == K_RIGHT:
        movement = player.check_movement(
            background.available_positions, "right")
    elif event.key == K_UP:
        movement = player.check_movement(
            background.available_positions, "up")
    elif event.key == K_DOWN:
        movement = player.check_movement(
            background.available_positions, "down")
    if movement != 0:
        # move the player
        player_rect = player_rect.move(movement)
        # check the new position of player with element
        if ((player.position[0] == element.position[0]) and (
                player.position[1] == element.position[1])):
            # update the counter
            counter_elts_founded += 1
            # Change element position
            new_element_position_x = element.position[0]
            new_element_position_y = element.position[1]
            while ((new_element_position_x == element.position[0]) and (
                    new_element_position_y == element.position[1])):
                element.position = choice(background.available_positions)
    return player, player_rect, element, counter_elts_founded
