def solution(number, k):
    answer = []
    temp = 0

    if int(number) == 0:
        return '0'
    if len(set(number)) == 1:
        return number[:-k]

    for i in range(len(number) - k):  # i만큼 append->answer의 길이만큼
        max_num = '0'
        for j in range(temp, k + i + 1):  # temp에서부터 k+i
            if (max_num < number[j]):
                max_num = number[j]
                temp = j + 1  # append한 위치 다음부터 두번째 for문 돌기
        answer.append(max_num)
    answer1 = "".join(answer)
    return answer1

print(solution("98765",2))
"""
#시간초과
from itertools import combinations 
def solution(number, k):
    n_split=[]
    n_comb=[]
    n_split=list(number)
    n_comb = list(combinations(n_split, len(n_split)-k))
    
    n_comb1=[0]*len(n_comb)
    for i in range(len(n_comb)):
        n_comb1[i]="".join(n_comb[i])
    
    answer=max(n_comb1)
    return answer
"""