def solution(x,n):
    if x>0:
        ans=[i+x for i in range(x*n) if i%x==0]
    else:
        ans = [i + x for i in range(x * n+1,1) if abs(i) % x == 0]
    return ans

print(solution(-4,2))

def solution2(x,n):
    if x>0:
        ans=[i for i in range(x,x*n+1,x)]
    else:
        ans = [i for i in range(x, x * n -1, x)]
    return ans

print(solution2(-4,2))


print([i for i in range(-8,0)])

a=[i+2 for i in range(2*5) if i%2==0]

print(a)
#2,5 [2,4,6,8,10]


