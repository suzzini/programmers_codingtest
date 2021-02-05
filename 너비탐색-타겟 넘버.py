"""
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
"""

numbers=[1,1,1,1,1]


def solution(numbers,sum+numbers[0],target):
    if(len(numbers)==0): #모든 경우의 수 끝, return값 더해주기
        if(sum==target): #다 돌았으니까
            return 1

    else:
        numbers.pop(0)
        sum=sum+numbers[0]
        return solution(numbers,sum,target)+solution(numbers,sum,target)

def get_value(numbers,value,target):
    if not numbers:
        if value==target:
            return 1
        return 0
    return get_value(numbers[1:],value+numbers[0],target)
            +get_value(numbers[1:],value-numbers[0],target)

def solution(numbers,target):
    return get_value(numbers[1:],numbers[0],target)+get_value(numbers[1:],numbers[0],target)



