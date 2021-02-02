#문자열 다루기 기본
def solution(s):
    try:
        int(s) #'a123'같이 영어가 있으면 에러 반환 시킴
        if len(s) in [4,6]:
            return True
        return False
    except: #try 구문 에러 나면 except 로 넘어옴
        return False
"""
for _s in s:
    if 48<=ord(_s)<=57:
        continue
    return False
    if len(s) in [4,6]:
        return True
    return False

print(solution('a123'))
"""

#문자열 내 마음대로 정렬하기
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
    # lambda 함수 , strings의 하나의 인덱스가 x가 됨,
    # 맨 처음 x[n]으로 정렬을 하고, 그 값이 같다면 x(사전순)로 정렬함.
    # sorted(strings)
    # sorted(strings, key=lambda x: x) 이 두개는 같음
    # strings = [123,12,123345]
    # sorted(strings,reverse=True)=sorted(strings, key=lambda x: -x)
    # key=lambda x: len(x)는 안됨, len 은 스트링에서만 가능

#가운데 글자 가져오기
def solution(s):
    my_s = list(s)
    x, y = divmod(len(s), 2)

    if y == 1:
        return s[x]
    else:
        return s[x - 1] + s[x]