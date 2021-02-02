import heapq

def scoville(first, second):
    return first + second * 2

def solution(scov, k):
    count = 0
    heapq.heapify(scov)
    while (scov[0] < k):
        min = heapq.heappop(scov)  # 지워지는 것도 포함
        scov.append(scoville(min, scov[0]))  # 두번째로 작은 인덱스에 접근하기 위함
        heapq.heappop(scov)
        count += 1

        if (scov[0] < k and len(scov) == 1):
            return -1

    return count