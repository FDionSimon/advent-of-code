from pyasn1_modules.rfc5280 import id_at_name


def main():
    print('-------------------')
    print(part_one('input.txt'))
    print('-------------------')
    print(part_two('input.txt'))
    print('-------------------')

def id_split(full_ids):
    id_one, id_two = full_ids.split('-')
    invalid_ids = []
    id_array = range(int(id_one), int(id_two))
    for id in id_array:
        string = str(id)
        length = len(string)
        mid = length // 2
        if string[:mid] == string[mid:]:
            invalid_ids.append(id)
    return invalid_ids

def id_repeat(full_ids):
    id_one, id_two = full_ids.split('-')
    invalid_ids = []
    id_array = range(int(id_one), int(id_two))
    for id in id_array:
        string = str(id)
        if string in (string + string)[1:-1]:
            invalid_ids.append(int(string))
    return invalid_ids

def file_to_list(input_file):
    with open(input_file, 'r') as file:
        input_list = file.read().split(',')
        file.close()
    return input_list

def invalid_counter(id_list, part):
    invalids = []
    for ids in id_list:
        if part == 1:
            reps = id_split(ids)
        if part == 2:
            reps = id_repeat(ids)
        invalids.extend(reps)
    return invalids

def part_one(input_file):
    input_list = file_to_list(input_file)
    invalid_ids = invalid_counter(input_list, 1)
    return sum(invalid_ids)

def part_two(input_file):
    input_list = file_to_list(input_file)
    invalid_ids = invalid_counter(input_list, 2)
    return sum(invalid_ids)

if __name__ == '__main__':
    main()
