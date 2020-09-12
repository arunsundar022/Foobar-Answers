def solution(n):
    n=int(n)
    step_count=0
    while n>1:
        if n & 1==0:
            n>>=1
        else:
            n = (n-1)if(n==3 or n%4==1) else(n + 1)
        step_count+=1
    return step_count
