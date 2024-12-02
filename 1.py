c=0
ll=[]
rl=[]
for i in range(1000):
    a,b=map(int,input().split())
    ll.append(a)
    rl.append(b)
for i in range(len(ll)):
    mll=ll.pop(ll.index(min(ll)))
    mrl=rl.pop(rl.index(min(rl)))
    c+=abs(mll-mrl)
print(c)