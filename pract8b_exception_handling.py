import sys
randomList = ['a',0,2,1.3]
for entry in randomList:
    try:
        print("The entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry")

print("The Reciprocal of ",entry,"is",r)
