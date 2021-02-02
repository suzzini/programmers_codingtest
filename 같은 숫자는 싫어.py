#ans의 마지막값과 arr 한번 훑기
def solution(arr):
    ans=[arr[0]]

    for _arr in arr[1:]: #1번쨰 인덱스부터 검사, 그리고 arr에 바로 접근하기
        if ans[-1].__ne__(_arr): #같지않다면 .__ne__
            ans.append(_arr)
    return ans