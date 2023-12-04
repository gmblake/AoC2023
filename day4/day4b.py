from collections import defaultdict

def main():
    total = 0
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    card_counts = defaultdict(int)
    for idx, line in enumerate(lines):
        card_counts[idx] += 1
        line = line.split(':')[1].split('|')
        line[1].strip('\n')
        winning_nums = set([int(s) for s in line[0].split()])
        card_nums = set([int(s) for s in line[1].split()])
        win_count = len(winning_nums & card_nums)
        for i in range(idx+1, idx + win_count+1):
            for _ in range(card_counts[idx]):
                card_counts[i] += 1
    
    total = sum(card_counts.values())
    print(f"Total: {total}")


if __name__ == "__main__":
    main()