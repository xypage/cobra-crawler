#
#  main.py
#
#  Created by Anthony Sainez on 7 February 2020
#  Copyright © 2020 Anthony Sainez. All rights reserved.
#

# Check out this resource
# https://docs.python.org/3/howto/curses.html

# TODO: Get board drawn so that characters are as tall as they are wide (i.e. a board made of squares)
# TODO: Draw actual walls
# TODO: Use inhertiance to put all the drawing functions outside of main.py (e.g. in draw.py)

import random
import curses

#snakeCharater = 'x'
#foodCharacter = 'f'

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), 'f')

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], 'f')
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), 'x')

# Code originated from https://github.com/engineer-man/youtube/blob/master/015/snake.py
