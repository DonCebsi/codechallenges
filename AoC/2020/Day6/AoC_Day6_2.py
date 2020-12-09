if __name__ == '__main__':
    # get input
    entries = [line.rstrip() for line in open("input_1.txt", "r")]

    # questionaire
    summe = 0
    answer = {}
    count = 0
    start = True
    for i in entries:
        if not i:
            # reset answers
            tmp = [k == count for k in answer.values()]
            summe += sum(tmp)
            answer = {}
            count = 0
            continue
        if count == 0:
            for j in i:
                answer[j] = 1
            count += 1
        else:
            for j in i:
                if j in answer:
                    answer[j] += 1
                else:
                    answer[j] = 1
            count += 1
    tmp = [k == count for k in answer.values()]
    summe += sum(tmp)
    print(summe)

