from itertools import permutations

def find_num(number):  # 소수 구하는 함수
    if number <= 1:  # 0, 1은 소수 x
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False  # 소수 아님
        return True

def solution(num):
    new_num = []
    for i in range(1, len(num) + 1):  # 조합구하기
        new_num.append(list(map(''.join, permutations(map(str, num), i))))  # str로 하는 이유가 뭐지 ??
        #=>('1',) 이렇게 나오는 것들 떄문에 int 형으로 map 할수가 없음

    final = []  # 중복 제거한 값 넣을 배열
    for i in new_num:  # 2차원 배열 모든 원소값에 접근하기 => 1차원 배열로 만들기
        for j in i:
            if int(j) not in final: #not in 해줬는데 중복제거 안되는 이유는?? => int(j)로 넣어줬기 떄문에 int() 해줘야함
                final.append(int(j))
    #print(final)
    # final=[int(i) for i in final] #int형으로 변환
    #final = list(set(final))  ##중복제거

    count = 0
    for i in final:
        if (find_num(i) == True):
            count += 1
    return count

print(solution("011"))


"""지은이코드
from itertools import permutations
import math

def get_prime_num(num, idx):
    sqrt_num = int(math.sqrt(num))
    print(sqrt_num)
    while sqrt_num >= idx:
        if num % idx == 0:
            return 0
        idx += 1
    return 0 if num == 1 else 1

def solution(numbers):
    nums = list(numbers)
    answer = 1 if '2' in nums else 0 #소수 중에 2는 소수임 , 그래서 2가 있다면 먼저 1 더해줌
    prmt_nums = set()
    for idx in range(1, len(nums)+1):
        prmt_nums.update(set(map(int, [''.join(num) for num in permutations(nums,idx)])))
    for prmt_num in prmt_nums:
        if prmt_num & 1 == 0:
            continue
        answer += get_prime_num(prmt_num, 3)
    return answer
"""