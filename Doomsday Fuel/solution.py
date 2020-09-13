def answer(matrix):
    matr=list(matrix)
    H=len(matrix)
    W=len(matrix[0])
    for i,elem in enumerate(matr):
        elem[i]=0
    sums=[sum(i) for i in matr]
    terms=[i for i,item in enumerate(sums) if item==0]
    not_terms=list((set(range(H)) - set(terms)))
    L=len(not_terms)
    for i in range(0,L-1):
        indB=not_terms[L-i-1]
        for j in range(0,L-1):
            indA=not_terms[j]        
            matr[indA]=fuse(matr[indA],indA,matr[indB],indB)
    output=[]
    for i in terms:
        output.append(matr[0][i])
    tot=sum(output)
    output.append(tot)
    if tot == 0:
        output=[1 for i in terms]
        output.append(len(terms))
    
    return output
def fuse(v1,i1,v2,i2):
    lenV=len(v1)
    indices=(set(range(lenV))-{i1,i2})
    sum2=sum(v2)
    out = [0 for i in v1]
    for i in indices:
        out[i]= sum2*v1[i]+v1[i2]*v2[i]
    gc=gcd_list(out)
    output = [int( i / gc ) for i in out ]
    return output
def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)
def gcd_list(lst):
    L=len(lst)
    out=0
    for i in range(0,L):
        out=gcd(out,lst[i])
    return out
