def is_float(s):
    for c in s:
        if not c.isdigit() and c != '.':
            return False
    return True


def main():
    filename = input('\ndata file name: ')
    f = open(filename)

    curr_nu = 0
    curr_de = 0

    types = list()
    percs = list()
    scores = list()

    for line in f:
        perc_p = line.find('counts as ') + 10

        if perc_p != 9:
            i = perc_p + 1

            while is_float(line[perc_p:i]):
                i += 1

            if curr_de != 0:
                scores.append(curr_nu / curr_de)
                curr_nu = curr_de = 0

            curr_perc = float(line[perc_p:i - 1])
            percs.append(curr_perc)
        else:
            line_split = line.split('\t')

            if len(line_split) == 1:
                type_name = line_split[0].split(' ')[0]
                types.append(type_name)
            elif len(line_split) == 4:
                try:
                    nu, de = int(line_split[2].split(' ')[0]), int(line_split[2].split(' ')[2])
                except:
                    pass
                else:
                    curr_nu += nu
                    curr_de += de

    if curr_de != 0:
        scores.append(curr_nu / curr_de)

    total_score = 0
    total_perc = sum(percs)
    scores = [x * 100 for x in scores]

    for i in range(len(types)):
        total_score += percs[i] * scores[i] / total_perc
        percs[i] = str(percs[i]) + '%'

    print('\nscore types: ', types)
    print('\nscore percentages: ', percs)
    print('\nindividual scores: ', scores)
    print('\ntotal score: ', total_score)


if __name__ == '__main__':
    main()
