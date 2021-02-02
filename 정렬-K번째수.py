array = [1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer=[]
    ans=[]
    for i,j,k in commands:
        answer=array[i-1:j] # i부터 j까지 짤라 넣기
        answer.sort() # 정렬
        #print([answer[k-1]]) #k번째 출력하기
        ans.append(answer[k-1])

    return ans