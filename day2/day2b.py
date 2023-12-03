
def main():    
    with open("input.txt", "r") as infile:
        total = 0
        while True:
            line = infile.readline()
            if not line:
                break

            max_red, max_green, max_blue = 0, 0, 0

            toks = [tok.strip(':,;') for tok in line.split()[2:]]
            
            for idx, tok in enumerate(toks[:-1]):
                if tok.isdigit():
                    if toks[idx+1] == "red":
                        if int(tok) > max_red:
                            max_red = int(tok)
                    elif toks[idx+1] == "green":
                        if int(tok) > max_green:
                            max_green = int(tok)
                    else:
                        if int(tok) > max_blue:
                            max_blue = int(tok)
            
            total += (max_red * max_green * max_blue)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()