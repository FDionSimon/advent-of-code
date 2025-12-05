def main():
    print(part_one('input.txt'))
    print(part_two('input.txt'))

def part_one(input_file):
    start = 50
    count = 0
    with open(input_file, 'r') as file:
        for line in file:
            if 'L' in line.strip():
                steps = int(line.strip()[1:])
                start = (start - steps) % 100
            elif 'R' in line.strip():
                steps = int(line.strip()[1:])
                start = (start + steps) % 100
            # Count exact
            if start == 0:
                count += 1
    return count

def part_two(input_file):
    start = 50
    count = 0
    with open(input_file, 'r') as file:
        for line in file:
            if 'R' in line.strip():
                steps = int(line.strip()[1:])
                start += steps
                count += int(start / 100)
                start %= 100
            elif 'L' in line.strip():
                steps = int(line.strip()[1:])
                last_start = start
                start -= steps
                if start == 0:
                    count += 1
                if start < 0:
                    if last_start != 0:
                        count += 1
                    count += int((steps - last_start) / 100)
                    start %= 100
    return count

if __name__ == '__main__':
    main()
