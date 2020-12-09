if __name__ == '__main__':
    # get input
    entries = [line for line in open("input_1.txt", "r")]

    # seatnumbers
    num = []
    for entry in entries:
        low = 0
        big = 127
        left = 0
        right = 7
        for i in range(7):
            if entry[i] == "F":
                big = (low+big)//2
            else:
                low = (low+big)//2 + 1
        for j in range(3):
            if entry[7+j] == "L":
                right = (left+right)//2
            else:
                left = (left+right)//2 + 1

        num.append(low*8+left)
    low = min(num)
    high = max(num)
    for i in range(70,826,1):
        if i not in num:
            print(i)
    print(low, high)

