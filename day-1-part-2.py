c=0
ll=[]
rl=[]
for i in range(1000):
    a,b=map(int,input().split())
    ll.append(a)
    rl.append(b)
for i in ll:
    c+=rl.count(i)*i
print(c)