def main():
    print('-------------------')
    print('Part One')
    print(route('input.txt', 1))
    print('-------------------')
    print('Part Two')
    print(route('input.txt', 2))
    print('-------------------')

def count_neighbours(input_array, row, col, target, max):
    # Directions NW,N,NE,W,E,SW,S,SE
    directions = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]
    hit = 0
    for dr, dc in directions:
        next_row = row + dr
        next_col = col + dc
        if 0 <= next_row < len(input_array) and 0 <= next_col < len(input_array[0]):
            if input_array[next_row][next_col] == target:
                hit += 1
                if hit > max:
                    return False
    return True

def find_roll(input_array):
    rolls = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            if input_array[i][j] != '@':
                continue
            if count_neighbours(input_array, i, j, '@', 3):
                rolls += 1
    return rolls


def find_roll_and_remove(input_array):
    rolls = 0
    while True:
        taken = []
        for i in range(len(input_array)):
            for j in range(len(input_array[i])):
                if input_array[i][j] != '@':
                    continue
                if count_neighbours(input_array, i, j, '@', 3):
                    taken.append((i, j))

        if not taken:
            break

        for k, l in taken:
            input_array[k][l] = '.'
            rolls += 1

    return rolls

def make_array_from_list(input_list):
    return [list(line) for line in input_list]

def parse_file(input_file):
    with open(input_file, 'r') as file:
        input_list = file.read().split('\n')
        file.close()
    return input_list

def route(input_file, part):
    input_list = parse_file(input_file)
    if part == 1:
        can_move = find_roll(make_array_from_list(input_list))
    if part == 2:
        can_move = find_roll_and_remove(make_array_from_list(input_list))
    return can_move

if __name__ == '__main__':
    main()
