from itertools import product

def solution(numbers, target):
    new_num = []
    check = []
    count = 0

    # product사용을 위한
    for i in range(len(numbers)):
        new_num.append([numbers[i], -numbers[i]])

    len_all = len(list(product(*new_num)))

    # 모든 경우의 수의 합을 check배열로 append
    for i in range(len_all):
        check.append(sum(list(product(*new_num))[i]))

    for i in check:
        if i == target:
            count += 1

    return count