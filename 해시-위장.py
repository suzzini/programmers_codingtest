from collections import Counter

def solution_s(clothes):
    x=Counter([clothe[1] for clothe in clothes])

    ans=1
    for i in x.values():
        ans=ans*(i+1)

    return ans-1

#지은이코드
from collections import Counter
from functools import reduce
def solution(clothes):
    return reduce(lambda x,y:(x)*(y), map(lambda x: x+1, Counter([clothe[1] for clothe in clothes]).values()))-1



""" 내가 원래했던거
from collections import defaultdict
from itertools import product

def solution(clothes):
    _dict = defaultdict(list)
    for v, k in clothes:
        _dict[k].append(v)

    answer = []  # 2차원 배열 형태로 저장
    for i in _dict.values():
        answer.append(i)

    _len=[]
    for i in range(len(answer)):
        _len.append(len(answer[i]))
    print(_len)

    ans=1
    for i in _len:
        ans=ans*(i+1

    return ans-1

clothes=[["crow_mask", "face"],
         ["blue_sunglasses", "face"],["gray","eye"] ,["smoky_makeup", "eye"],["black","face"]]

print(solution(clothes))"""