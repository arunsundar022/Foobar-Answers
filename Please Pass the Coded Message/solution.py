from itertools import combinations
def solution(l):
    l.sort(reverse=True)
    for i in reversed(range(1,len(l)+1)):
        for j in list(combinations(l,i)):
            if sum(j)%3==0:
                return int(''.join(map(str,j)))
    return 0