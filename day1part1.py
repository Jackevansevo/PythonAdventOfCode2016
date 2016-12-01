from collections import deque


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance_from_origin(self):
        return(sum(map(abs, [self.x, self.y])))


def read_input(file):
    with open(file) as f:
        return f.read().strip().split(', ')


if __name__ == '__main__':

    instructions = read_input('puzzleInputs/day1input.txt')
    directions = deque('NESW')
    coords = Point(0, 0)

    for instruction in instructions:
        rotation, *steps = instruction

        # Handle the direction
        directions.rotate(1) if rotation == 'R' else directions.rotate(-1)

        # Move santa
        steps = int(''.join(steps))

        direction_funcs = {
            'N': lambda: setattr(coords, 'y', coords.y + steps),
            'E': lambda: setattr(coords, 'x', coords.x + steps),
            'S': lambda: setattr(coords, 'y', coords.y - steps),
            'W': lambda: setattr(coords, 'x', coords.x - steps),
        }
        direction_funcs[directions[0]]()

    print(coords.distance_from_origin)
