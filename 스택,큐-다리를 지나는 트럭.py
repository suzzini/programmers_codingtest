
#디큐 사용, 인덱스0의 원소 찾는 시간복잡도 O(1)

#시간 int형으로 while문 때마다 +1
#계속돌아가는 시간 -트럭이 다리를 들어갈때 시간=다리의 길이 : 다 건넘
#길이 체크 후 weight 체크 이 다리가 건널수 잇는지 없는지

#마지막 트럭은 그냥 다리의 길이만큼 더해줘서 출력시킴

    #트럭 하나가 지나가는데 총 bridge_length초 만큼 소요됨
    #그 때, 무게가 weight을 넘지 않는 다면 뒤에 트럭도 건너도 됨
    #다리를 건너고 있는 트럭을 표시해주는 배열 필요
    #다 완료된 트럭을 표시하기 위해 truck 배열에서 pop 해주기
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck = deque(truck_weights)
    bridge = deque([])
    _weight = 0
    while truck:
        time += 1
        #truck.popleft() 하면 인덱스 0 출력
        #append




    return time + bridge_length


print(solution(2,10,[7,4,5,6]))