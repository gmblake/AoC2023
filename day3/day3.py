
def main():
    with open("input.txt", "r") as infile:
        lines = infile.readlines()
    total = 0
    seen_xys = set()

    '''
    ..., (x - 1, y - 1), (    x, y - 1), (x + 1, y - 1), ...
    ..., (x - 1,     y), (    x,     y), (x + 1,     y), ...
    ..., (x - 1, y + 1), (    x, y + 1), (x + 1, y + 1), ...
    '''
    def _get_num(x, y):
        # assumes valid indices
        if not lines[y][x].isdigit():
            return 0
        
        start_idx, end_idx = x, x
        
        # get digits before
        while True:
            if start_idx - 1 < 0 or not lines[y][start_idx - 1].isdigit():
                break
            start_idx -= 1
        
        if (start_idx, y) in seen_xys:
            return 0
        
        # get digits afer
        while True:
            if end_idx + 1 >= len(lines[y]) or not lines[y][end_idx + 1].isdigit():
                break
            end_idx += 1
        
        seen_xys.add((start_idx, y))
        return int(lines[y][start_idx:end_idx+1])

    for y, line in enumerate(lines):
        for x, sym in enumerate(line):
            if sym not in {'.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'}:
                # Upper left
                if x > 0 and y > 0:
                    total += _get_num(x-1, y-1)
                # Above
                if y > 0:
                    total += _get_num(x, y-1)
                # Upper right
                if x < len(line) - 1 and y > 0:
                    total += _get_num(x+1, y-1)
                # Left
                if x > 0:
                    total += _get_num(x-1, y)
                # Right
                if x < len(line) - 1:
                    total += _get_num(x+1, y)
                # Lower left
                if x > 0 and y < len(lines) - 1:
                    total += _get_num(x-1, y+1)
                # Below
                if y < len(lines) - 1:
                    total += _get_num(x, y+1)
                # Lower right
                if x < len(line) - 1 and y < len(lines) - 1:
                    total += _get_num(x+1, y+1)

    print(f"Total: {total}")
    import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()