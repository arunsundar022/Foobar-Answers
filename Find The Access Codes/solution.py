def solution(l):
    l_size=len(l)
    cnt=0
    while l_size>=2:
        l_size-=1
        cnt+=len(multiples(l,l_size))*len(dividers(l,l_size))
    return cnt
    
def multiples(l,ind):
    cur_ind=l[ind]
    return [i for i in l[ind+1:] if i%cur_ind==0]

def dividers(l,ind):
    cur_ind=l[ind]
    return [i for i in l[:ind] if cur_ind%i==0]
