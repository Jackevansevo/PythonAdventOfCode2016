def read_input(file):
    with open(file) as f:
        return f.read().strip().split(', ')


if __name__ == '__main__':

    # [TODO] Fix this abomination

    instructions = read_input('puzzleInputs/day1input.txt')
    directions = ('N', 'E', 'S', 'W')
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
            y += steps

        if directions[direction] == 'E':
            x += steps

        if directions[direction] == 'S':
            y -= steps

        if directions[direction] == 'W':
            x -= steps

    print(abs(x) + abs(y))
