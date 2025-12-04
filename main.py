def main():
    print('-------------------')
    print('Part One')
    print(route('test.txt', 1))
    # print(route('input.txt', 1))
    print('-------------------')
    # print('Part Two')
    # print(route('input.txt', 2))
    # print('-------------------')

def find_roll(row, row_index, input_list):
    hit = 0
    others = 0
    for char in range(len(row)):
        if row[char] == '@':
            if len(input_list) >  row_index > 0:
                same_row = row[char - 1] + row[char + 1]
                row_above = input_list[row_index[char - 1]  - 1] + input_list[row_index[char]  - 1] + input_list[row_index[char + 1] - 1]
                row_below = input_list[row_index[char - 1]  + 1] + input_list[row_index[char]  + 1] + input_list[row_index[char + 1] + 1]
            elif row_index == 0:
                same_row = row[char - 1] + row[char + 1]
                row_below = input_list[row_index[char - 1]  + 1] + input_list[row_index[char]  + 1] + input_list[row_index[char + 1] + 1]
            all_surrounding_chars = same_row + row_above + row_below
            print(all_surrounding_chars)
            hit += 1
    return hit

def check_rows(input_list, part):
    rolls = 0
    for row in input_list:
        if part == 1:
            print(input_list.index(row))
            rolls += find_roll(row, input_list.index(row), input_list)
    return rolls


def parse_file(input_file):
    with open(input_file, 'r') as file:
        input_list = file.read().split('\n')
        file.close()
    return input_list

def route(input_file, part):
    input_list = parse_file(input_file)
    can_move = check_rows(input_list, part)
    return can_move

if __name__ == '__main__':
    main()
