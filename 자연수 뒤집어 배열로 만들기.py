def solution(n):
    n = str(n)
    answer = []
    for i in n:
        answer.insert(0, int(i))

    return answer

def solution(n):
    return list(map(int,str(n)[::-1]))
#[::-1] 뒤집겟다는 거
# list('54321') => ['5','4','3','2','1']
# reduce((lambda x,y : x+y), [x for x in range(1,101)])