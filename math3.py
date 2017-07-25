pi="3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862"
#pi="3.1415926535"
f=[]
for i in range(len(pi)-2):
    f.append(pi[2+i:4+i])
f.sort()
g=""
n=0
for x in range(100,200):
    g=str(x)[1:3]
    n=f.count((str(x))[1:])
    ff=dict()
    ff[g]=n
    print(ff)