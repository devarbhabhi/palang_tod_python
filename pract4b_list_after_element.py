color=['red','green','white','black','pink','yellow']
color1=[]
for(i,x) in enumerate(color):
    if i in (0,4,5):
        continue
    color1.append(x)
print(color1)
