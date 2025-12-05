import utils.basic_helpers as bh

def main():
    bh.basic_text('input.txt', 'one')

#### START ####

def part_one(input_list):
    result = input_list
    return result

def part_two(input_list):
    result = input_list
    return result

#### END ####

def route(input_file, part):
    input_list = bh.parse_file(input_file)
    result = 0
    if part == 1:
        result = part_one(input_list)
    if part == 2:
        result = part_two(input_list)
    return result

if __name__ == '__main__':
    main()
