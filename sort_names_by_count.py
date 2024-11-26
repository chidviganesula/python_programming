//8. takes names and print w.r.t their count and sort them acc to names
l=list(map(int,input().split(',')))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(dict(sorted(d.items())))

// if u want to sort acc to values

l=list(map(int,input().split(',')))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    d1={}
    d1[d[i]]=i
print(dict(sorted(d.items())))
