def solution(n, lost, reserve):
    n_reserve=sorted(list(set(lost)-set(reserve)))
    n_lost = sorted(list(set(reserve)-set(lost)))
    print(n_lost, n_reserve)

    count = 0
    for i in range(len(n_lost)):  # 0,1
        for j in range(len(n_reserve)):  # 0,1,2
            if (n_reserve[j] - 1 == n_lost[i] or n_reserve[j] + 1 == n_lost[i]):
                count += 1
                n_reserve.pop(j)
                break

    return n if n_lost==n_reserve else n-len(n_lost)+count

print(solution(5,[2,4],[1,3,5]))

#지은이 코드
def solution(n, lost, reserve):
    lost_list = sorted(list(set(lost).difference(set(reserve))))
    reserve_list = sorted(list(set(reserve).difference(set(lost))))
    for l in lost_list:
        if l-1 in reserve_list:
            reserve_list.remove(l-1)
            continue
        elif l+1 in reserve_list:
            reserve_list.remove(l+1)
            continue
        n-=1
    return n

