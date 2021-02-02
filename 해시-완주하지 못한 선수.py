def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        # zip 함수 a = [1,2,3], b = [4,5,6,7]
        # zip(a,b) = [[1,4], [2,5], [3,6]], 7은 묶이지 않고 버려짐
        # print(p,c)
        if p!=c: # 같지 않다는 것은 정답
            return p
    # 그러나, 혹시 완주를 못한 애가 맨뒤에 있으면 p!=c에 안걸림, 버려졌다는 뜻
    return participant[-1] # 정렬된 마지막 인덱스 출력