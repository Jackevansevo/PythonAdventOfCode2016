class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance_from_origin(self):
        return(sum(map(abs, [self.x, self.y])))

    def __str__(self):
        return ('Point({}, {})'.format(self.x, self.y))


def read_input(file):
    with open(file) as f:
        return f.read().strip().split(', ')


if __name__ == '__main__':

    instructions = read_input('puzzleInputs/day1input.txt')
    directions = ('N', 'E', 'S', 'W')
    coords = Point(0, 0)
    x, y = 0, 0
    direction = 0

    for instruction in instructions:

        rotation, *steps = instruction

        # Handle the direction
        if rotation == 'R':
            if direction == 3:
                direction = 0
            else:
                direction += 1
        else:
            if direction == 0:
                direction = 3
            else:
                direction -= 1

        # Move santa
        steps = int(''.join(steps))

        if directions[direction] == 'N':
            coords.y += steps
            y += steps

        if directions[direction] == 'E':
            coords.x += steps
            x += steps

        if directions[direction] == 'S':
            coords.y -= steps
            y -= steps

        if directions[direction] == 'W':
            coords.x -= steps
            x -= steps

    print(coords.distance_from_origin)
