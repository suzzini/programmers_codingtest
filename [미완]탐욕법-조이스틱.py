


name='ZAQAAAZ'
distance=[min(ord(i)-ord("A"),ord("Z")-ord(i)+1) for i in name]
#A 또는 Z까지의 길이 중 최솟값 출력

_name=[i for i in name]
print(_name)
#print(_name[1]=='A')

#l_c, r_c
#count=[]
l_c=0
r_c=0
while 1:
    for i in range(len(_name)-1): #0,1,2,3,4,5
        l_c-=1
        if(_name[-(i+1)]=='A'): #-1, -2,-3,-4,-5,-6
            break
print(l_c)