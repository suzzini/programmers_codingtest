def solution(s):
    if s.upper().count("P") == s.upper().count("Y"):
        return True
    else:
        return False

    # return True if s.upper().count("P")==s.upper().count("Y") return False else:


from collections import  Counter
def solution(s):
    s_count = Counter(s.lower())
    return True if s_count['p'] == s_count['y'] else False