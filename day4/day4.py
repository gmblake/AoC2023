
def main():
    total = 0
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    for line in lines:
        line = line.split(':')[1].split('|')
        line[1].strip('\n')
        winning_nums = [int(s) for s in line[0].split()]
        card_nums = [int(s) for s in line[1].split()]
        total += int(2 ** (len([n for n in card_nums if n in winning_nums]) - 1))

    print(f"Total: {total}")


if __name__ == "__main__":
    main()