if __name__ == '__main__':
    # get input
    entries = [int(line.strip()) for line in open("input_1.txt", "r")]

    # sort list
    entries.sort()

    # find 2 numbers that add to 2020
    idx1 = 0
    idx2 = -1
    while entries[idx1]+entries[idx2] != 2020:
        if entries[idx1]+entries[idx2] > 2020:
            idx2 -= 1
        elif entries[idx1]+entries[idx2] < 2020:
            idx1 += 1

    print(entries[idx1]*entries[idx2])
