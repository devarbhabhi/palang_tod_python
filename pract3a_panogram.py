def Panagram(nf):
    check="abcdefghijklmnopqrstuvwxyz"
    for l in check:
        if(l in nf):
            continue
        else:
            return True
        return False
n=input("Enter the any Text:")
if(Panagram (n.lower())):
    print("No it is Not a Panagram")
