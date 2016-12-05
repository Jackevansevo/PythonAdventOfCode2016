import numpy as np


# [TODO] Make Board class with Point instances

class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, attr, val):
        if 0 <= val <= 2:
            super(Point, self).__setattr__(attr, val)

    def __str__(self):
        return 'Point({}, {})'.format(self.x, self.y)


def read_input(file):
    with open(file) as f:
        return [l.strip() for l in f.readlines()]


if __name__ == '__main__':
    instructions = read_input('puzzleInputs/day2input.txt')

    grid = np.arange(1, 10).reshape((3, 3)).tolist()
    coords = Point(1, 1)
    code = []

    for line in instructions:
        for command in line:
            direction_funcs = {
                'U': lambda: setattr(coords, 'x', coords.x - 1),
                'R': lambda: setattr(coords, 'y', coords.y + 1),
                'D': lambda: setattr(coords, 'x', coords.x + 1),
                'L': lambda: setattr(coords, 'y', coords.y - 1),
            }
            direction_funcs[command]()
        code.append(grid[coords.x][coords.y])

    print(code)
