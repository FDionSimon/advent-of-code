def main():
    print('-------------------')
    print('Part One')
    print(route('input.txt', 1))
    print('-------------------')
    print('Part Two')
    print(route('input.txt', 2))
    print('-------------------')

def highest_combo(bank, chars):
    bank_length = len(bank)
    usable = bank_length - chars
    highest = []
    for digit in bank:
        while highest and highest[-1] < digit and usable > 0:
            highest.pop()
            usable -= 1
        highest.append(digit)
    return ''.join(highest[:chars])

def bepale_big_joltage(bank):
    joltage = highest_combo(bank, 12)
    return int(joltage)

def bepale_joltage(bank):
    joltages = []
    for digit_one in range(len(bank)):
        for digit_two in range(digit_one + 1, len(bank)):
            digit = bank[digit_one] + bank[digit_two]
            joltages.append(digit)
    return int(max(joltages))

def parse_banks(banks, part):
    total_joltage = 0
    for bank in banks:
        if part == 1:
            total_joltage += bepale_joltage(bank)
        if part == 2:
            total_joltage += bepale_big_joltage(bank)
    return total_joltage

def file_to_list(input_file):
    with open(input_file, 'r') as file:
        input_list = file.read().split('\n')
        file.close()
    return input_list

def route(input_file, part):
    input_list = file_to_list(input_file)
    res = parse_banks(input_list, part)
    return res

if __name__ == '__main__':
    main()
