
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
            if sym == '*':
                seen_xys.clear()
                parts = []
                # Upper left
                if x > 0 and y > 0:
                    parts.append(_get_num(x-1, y-1))
                # Above
                if y > 0:
                    parts.append(_get_num(x, y-1))
                # Upper right
                if x < len(line) - 1 and y > 0:
                    parts.append(_get_num(x+1, y-1))
                # Left
                if x > 0:
                    parts.append(_get_num(x-1, y))
                # Right
                if x < len(line) - 1:
                    parts.append(_get_num(x+1, y))
                # Lower left
                if x > 0 and y < len(lines) - 1:
                    parts.append(_get_num(x-1, y+1))
                # Below
                if y < len(lines) - 1:
                    parts.append(_get_num(x, y+1))
                # Lower right
                if x < len(line) - 1 and y < len(lines) - 1:
                    parts.append(_get_num(x+1, y+1))
                
                parts = [part for part in parts if part > 0]

                if len(parts) == 2:
                    total += parts[0] * parts[1]

    print(f"Total: {total}")


if __name__ == "__main__":
    main()