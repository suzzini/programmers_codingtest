import math
def solution(progress, speeds):
    r_days = []
    days = []

    # 남은 작업일 수 구하기
    for i, j in list(zip(progress, speeds)):
        r_days.append(math.ceil((100 - i) / j))

    temp = r_days[0]
    func_count = 1

    for i in range(1, len(r_days)):
        if (temp < r_days[i]):
            temp = r_days[i]
            days.append(func_count)
            func_count = 1
        else:
            func_count += 1

    days.append(func_count)

    return days