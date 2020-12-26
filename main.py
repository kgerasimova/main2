def solution(a=list):
    n=0
    mis=0
    for i in a:
        n+=1
    lt=[i for i in range(n+1)]
    for i in lt:
        if i not in a:
            mis=i
    return mis
