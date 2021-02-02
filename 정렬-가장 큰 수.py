def solution(numbers):
    ans = []
    numbers = list(map(str, numbers))
    max_num = len(max(numbers, key=lambda x: len(x)))  # 가장 긴 길이 구하기

    def leng(x):
        while len(x) < 4:
            x += x
        return int(x[:4])

    for i in range(len(numbers)):
        ans.append([numbers[i], leng(numbers[i])])

    ans = sorted(ans, key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in ans]
    answer = "".join(answer)

    if answer[0] == '0':
        return '0'

    return answer

print(solution([3, 30, 34, 5, 9]))


from itertools import permutations #시간 초과
def solution1(numbers):
    ans=list(map(str,numbers))
    ans1=list(permutations(ans,len(numbers))) #모든 경우의 수 구하기

    answer=[0]*len(ans1)

    for i in range(len(ans1)):
        answer[i]="".join(ans1[i])
    #print(answer[0])
    return str(max(answer))

num=[11,234,5]
print(solution1(num))
