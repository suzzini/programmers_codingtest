
#max면 뺴주고 max가 아니면 뒤로뺴주기
#pop하는 순간 answer가 +1이 되어야함
#location을 계속해서 추적
#1,1,9,1,1,1 을 정리해서 9,1,1,1,1,1 하면


def solution1(pri, location):
    max_num=max(pri)

    for i in range(len(pri)):
        if pri[0]<max_num:
            pri.insert(len(pri), pri[0])
            pri.pop(0)
            location-=1 #location -2
    print(pri,location)

    if location==0:
        return 1
    else:
        answer=len(pri)-abs(location)
        return answer+1
print(solution1([2,1,3,2],2))

def solution(pri, location):
    abc = [chr(65 + i) for i in range(len(pri))]  # A B C D
    answer=abc[location] #알파벳 C저장
    print(abc)
    for i in range(len(pri)):  # 0,1,2,3,4,5
        for j in range(i+1, len(pri)):
            if (pri[i] < pri[j]):  # pri, 한개라도 중요도 높은 문서가 존재하면
                abc.insert(len(abc), abc[i])
                abc.pop(i)
                pri.insert(len(abc), pri[i])
                pri.pop(i)
                print(i,j)
                print(abc)
                print(pri)
                break
    print(abc)
    return abc.index(answer)+1

print(solution([2,1,2,1,3,2],0))
