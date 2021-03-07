




import re
def solution(new_id):
    #1단계
    answer=new_id.lower()

    #2단계
    answer = re.sub(r'[^ \nA-Za-z0-9-_.]+', '', answer)

    #3단계
    answer= re.sub("\.{2,}",".", answer)  # .가 2개 이상이면 . 하나로 바꾸기

    # 4단계
    if (answer == ''): #빈공백일경우
        answer = answer
    elif(answer[0]=='.'):
        answer=answer[1:]

    if(answer==''):#빈공백일경우
        answer=answer
    elif(answer[-1] == '.'):
        answer = answer[0:-1]

    #5단계
    if(answer==""):
        answer='a'

    #6단계
    if(len(answer)>=16):
        answer=answer[0:15]
    if(answer[-1]=='.'):
        answer = answer[0:-1]

    #7단계
    if (len(answer) <=2):
        while(len(answer)<3):
            answer+=answer[-1]
            if(len(answer)==3):
                break

    return answer

print(solution("abcdefghijklmn.p"))

