if __name__ == '__main__':
    # get input
    entries = [line for line in open("input_1.txt", "r")]

    # combine lines to one entry per passport
    input = []
    passport = ""
    for line in entries:
        if line != "\n":
            passport += line + " "
        elif line == "\n":
            input.append(passport)
            passport = ""

    input.append(passport)
    count = 0
    # create a dict for better visuality
    t = []
    for i in input:
        tmp = i.split()
        dic = dict()
        for j in tmp:
            k, l = j.split(":")
            dic[k] = l
        t.append(dic)
    hcls = "0123456789abcdef"
    ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for entry in t:
        if len(entry) < 7:
            continue
        else:
            # check for valid entries
            # no cid in an entry with 7 attributes
            if len(entry) == 7:
                if "cid" in entry:
                    continue

            # check for attribute validation
            if not (1920 <= int(entry['byr']) <= 2002):
                print(entry['byr'])
                continue
            if not (2010 <= int(entry['iyr']) <= 2020):
                continue
            if not (2020 <= int(entry['eyr']) <= 2030):
                continue
            # check for cm or in
            if "cm" in entry['hgt']:
                if not (150 <= int(entry['hgt'][:-2]) <= 193):
                    continue
            elif "in" in entry['hgt']:
                if not (59 <= int(entry['hgt'][:-2]) <= 76):
                    continue
            else:
                continue
            # hair color
            if entry['hcl'][0] == "#":
                if not (all(c in hcls for c in entry['hcl'][1:])):
                    continue
            else:
                continue
            # eye color
            if not (entry['ecl'] in ecls):
                continue
            # pid
            if len(entry['pid']) == 9:
                try:
                    number = int(entry['pid'])
                except ValueError:
                    continue
        count += 1
    print(count)

