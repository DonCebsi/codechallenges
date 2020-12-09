if __name__ == '__main__':
    # get input
    entries = [line for line in open("input_1.txt", "r")]

    # combine lines to one entry per passport
    input = []
    passport = ""
    for line in entries:
        if line != "\n":
            passport += line[:-2] + " "
        elif line == "\n":
            input.append(passport[:-1])
            passport = ""

    input.append(passport[:-1])
    count = 0

    for inp in input:
        tmp = inp.split()
        if len(tmp) == 7:
            counting = True
            for i in tmp:
                if "cid:" in i:
                    counting = False
            if counting:
                count += 1
        if len(tmp) == 8:
            count += 1

    print(count)

