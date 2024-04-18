def get_nums(data):
    num_list = []
    new_num = ''
    inds = []
    for a, i in enumerate(data):
        for b, ii in enumerate(i):
            #print(ii)
            if ii.isnumeric():
                new_num += ii
                inds.append(str(a) + ':' + str(b))
            else:
                if new_num:
                    num_list.append(new_num + '|' + '-'.join(inds))
                    new_num = ''
                    inds = []
    return num_list


def num_check(num_ind, line_li):
    num, ind = int(num_ind.split('|')[0]), num_ind.split('|')[1]
    test_arr = [-1, 0, 1]
    for iii in ind.split('-'):
        try:
            x, y = int(iii.split(':')[0]), int(iii.split(':')[1])
            for iv in test_arr:
                for v in test_arr:
                    if not line_li[x + iv][y + v].isnumeric() and line_li[x + iv][y + v] != '.':
                        #print(num)
                        return num
        except IndexError:
            continue
    return 0


f = open("./func_test_data2.txt")
lines = f.readlines()
nums = get_nums(lines)
total = 0
for ab in nums:
    total += num_check(ab, lines)

print(total)
