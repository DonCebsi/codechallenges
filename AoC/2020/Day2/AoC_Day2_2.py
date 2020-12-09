def valid(rule, pw):
    rule_amount, rule_char = rule.split(" ")
    pos1, pos2 = map(int, rule_amount.split("-"))
    if pw[pos1] == rule_char and pw[pos2] == rule_char:
        return False
    if pw[pos1] == rule_char:
        return True
    if pw[pos2] == rule_char:
        return True
    return False


if __name__ == '__main__':
    # get input
    entries = [line.strip() for line in open("input_1.txt", "r")]

    # find number of valid password
    count = 0
    while entries:
        entry = entries.pop()
        rule, pw = entry.split(":")
        if valid(rule, pw):
            count += 1

    print(count)
