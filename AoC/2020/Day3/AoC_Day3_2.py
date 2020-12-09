if __name__ == '__main__':
    # get input
    entries = [line.strip() for line in open("input_1.txt", "r")]
    # get movement
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    # traverse
    trees = []
    for move in moves:
        x, y = move
        position = 0
        count = 0
        row = 0
        for i in entries:
            if row % y != 0:
                row += 1
                continue
            if i[position] == "#":
                count += 1
            position = (position+x) % len(entries[0])
            row += 1
        trees.append(count)
        print(count)
    res = 1
    for tree in trees:
        res *= tree
    print(res)
