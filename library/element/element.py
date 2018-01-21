#! /usr/bin/env python3
# coding: utf-8

""" Module with class Element"""

# pylint: disable=too-few-public-methods


class Element():
    """ game's element with a position, a path to the
    corresponding image and his size, and a feature"""

    def __init__(self, img, position, feature, size_img):
        """create an element with
        img :  str 'path/to/image'
        position: tuple (x, y)
        feature:  str 'player' or 'recoverable' or 'end'
        size_img : tuple (x, y)"""
        self.img = img
        self.position = position
        self.feature = feature
        self.size_img = size_img

    def check_movement(self, available_positions, direction):
        """check if movement in a direction is available,
        update the element position and return the movement.
        available_positions : list of tuples (x,y)
        direction : str 'left', 'right', 'up', 'down'"""

        # set position before the movement
        new_position_x = self.position[0]
        new_position_y = self.position[1]
        movement_x = 0
        movement_y = 0
        # find the diection
        if direction == "left":
            # update position after movement
            new_position_x -= self.size_img[0]
            movement_x = (-self.size_img[0])
        elif direction == "right":
            new_position_x += self.size_img[0]
            movement_x = self.size_img[0]
        elif direction == "up":
            new_position_y -= self.size_img[1]
            movement_y = -self.size_img[1]
        elif direction == "down":
            new_position_y += self.size_img[1]
            movement_y = self.size_img[1]
        # check the new position ...
        new_position = (new_position_x, new_position_y)
        if new_position in available_positions:
            # update position
            self.position = new_position
            # return the movement
            return movement_x, movement_y
        return 0
