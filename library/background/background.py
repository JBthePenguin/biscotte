#! /usr/bin/env python3
# coding: utf-8

""" Module with class Labyrinth"""


class Background(dict):
    """game's background is from class dict with
    positions(key) of wall or floor(values) {(x,y), 'wall or floor'},
    and have as property a list of available positions,
    size for window's gui and a position for the counter"""

    def __init__(self, map_file, wall, floor, size_img):
        """create a background with
        map_file : str 'path/to/file.txt'
        wall: str 'path/to/image'
        floor : str 'path/to/image'
        size_img : tuple (x, y)"""

        # initialize a available positions and size window
        dict.__init__(self)
        self.available_positions = []
        # read the .txt with the background
        with open(map_file, "r") as bg_file:
            # Initialize position and number of lines
            nbre_lines = 1
            position_x = 0
            position_y = 0
            # read character by character
            for elt in bg_file.read():
                if elt == "\n":
                    nbre_lines += 1
                    # update next position
                    position_x = 0
                    position_y += size_img[1]
                else:
                    # get corresponding image
                    if elt == "O":
                        # add key (x,y) and value img in background
                        self[(position_x, position_y)] = wall
                    else:
                        self[(position_x, position_y)] = floor
                        # update available positions
                        self.available_positions.append(
                            (position_x, position_y))
                    # update position
                    position_x += size_img[0]
        # set the size of the window for gui and the counter position
        size_window_x = int((len(self) / nbre_lines) * size_img[0])
        size_window_y = int(position_y + (2 * size_img[1]))
        self.size_window = (size_window_x, size_window_y)
        self.counter_position = (0, (size_window_y - size_img[1]))
