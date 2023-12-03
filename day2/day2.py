import os


def main():

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    with open("input.txt", "r") as infile:
        total = 0
        while True:
            line = infile.readline()
            if not line:
                break

            toks = [tok.strip(':,;') for tok in line.split()[1:]]
            game_id = int(toks[0])
            toks = toks[1:]
            
            bad_line = False
            for idx, tok in enumerate(toks[:-1]):
                if tok.isdigit():
                    if int(tok) > limits[toks[idx+1]]:
                        bad_line = True
                        break
            
            if not bad_line:
                total += game_id

    print(f"Total: {total}")


if __name__ == "__main__":
    main()