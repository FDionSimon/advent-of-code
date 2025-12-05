def basic_text(input_file, parts):
    if parts == 'one' or parts == 'full':
        print('-------------------')
        print('Part One')
        print(route(input_file, 1))
    if parts == 'two' or parts == 'full':
        print('-------------------')
        print('Part Two')
        print(route(input_file, 2))
        print('-------------------')

def make_array_from_list(input_list):
    return [list(line) for line in input_list]

def parse_file(input_file):
    with open(input_file, 'r') as file:
        input_list = file.read().split('\n')
        file.close()
    return input_list
