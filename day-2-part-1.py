c=0
t1 = lambda l: all(l[i]<l[i+1] for i in range(len(l)-1)) or all(l[i]>l[i+1] for i in range(len(l)-1))
def t2(l):
    if len(l)<2:
        return False
    for i in range(len(l)-1):
        diff = abs(l[i+1]-l[i])
        if not (1<=diff<=3):
            return False
    return True
for i in range(1000):
    l=list(map(int,input().split()))
    diffs = [l[i+1]-l[i] for i in range(len(l)-1)]
    if t2(l)==True and t1(l)==True:
        c+=1
print(c)