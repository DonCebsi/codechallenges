if __name__ == '__main__':
    # get input
    entries = [line.rstrip() for line in open("input_1.txt", "r")]

    # questionaire
    sum = 0
    answer = ""
    for i in entries:
        if not i:
            # reset answers
            sum += len(answer)
            answer = ""
        for j in i:
            if j not in answer:
                answer += j
    sum += len(answer)
    print(sum)

