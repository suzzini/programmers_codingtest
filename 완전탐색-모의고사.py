#파이썬 딕셔너리 {key:value,...}
#student={1:[1,2,3,4,5],2:[2,1,2,3,2,4,2,5],3:[3,3,1,1,2,2,4,4,5,5]}
#for values in student.keys():
#   print(values)
#for key, value in student.items()

def solution(answers):
    answer = []
    test1 = [1, 2, 3, 4, 5]
    test2 = [2, 1, 2, 3, 2, 4, 2, 5]
    test3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for i in range(len(answers)):
        if test1[i % len(test1)] == answers[i]:
            count[0] += 1
        if test2[i % len(test2)] == answers[i]:
            count[1] += 1
        if test3[i % len(test3)] == answers[i]:
            count[2] += 1

    max_count = max(count)

    answer = [i + 1 for i in range(3) if max_count == count[i]]

    return answer