if __name__ == '__main__':
    # get input
    entries = [line.strip() for line in open("input_1.txt", "r")]
    # traverse
    position = 0
    count = 0
    for i in entries:
        if i[position] == "#":
            count += 1
        position = (position+3) % len(entries[0])
    print(count)
