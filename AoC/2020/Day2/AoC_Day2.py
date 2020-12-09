def valid(rule, pw):
    rule_amount, rule_char = rule.split(" ")
    least, most = map(int, rule_amount.split("-"))
    occurence = pw.count(rule_char)
    if least <= occurence <= most:
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
