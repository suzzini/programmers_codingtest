def solution(prices):
    len_price = len(prices)
    answer = [0]*len_price
    for i in range(len_price-1):
        for j in range(i,len_price-1):
            if prices[i]>prices[j]:
                break
            else:
                answer[i]+=1
    return answer
