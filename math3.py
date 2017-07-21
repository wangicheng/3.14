pi="3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862"
f=[]
for i in range(1,len(pi)-2):
    f.append(pi[2+i:4+i])
f.sort()
g=[]
n=[]
for x in range(100,200):
    g.append((str(x))[1:])
    n.append(f.count((str(x))[1:]))
print(dict(zip((g), (n))))