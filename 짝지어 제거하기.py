def solution(s):
    a = []

    for i in s:
        if len(a)==0: # 처음이나 중간에 다 지워질 경우, 스택이 비면 무조건 append 하기
            a.append(i)
        elif i==a[-1]: # 최근에 들어간 것과 비교
            a.pop()
        else: #둘다 아니라면 a에 append
            a.append(i)

    if len(a)==0: #비워져잇으면
        return 1
    else:
        return 0

