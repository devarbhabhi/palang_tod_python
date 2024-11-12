nterms=int(input("How many terms?"))
n1=0
n2=1
count=2
#check if number of terms is valid
if nterms<=0:
    print("Please enter a Positive Integer")
elif nterms==1:
    print("Fibanacci Sequence upto",nterms,":")
    print(n1)
else:
    print("Fibanacci Sequence upto",nterms,":")
    print(n1,",",n2,end=",")
while count<nterms:
    nth=n1+n2
    print(nth,end=",")
    n1=n2
    n2=nth
    count+=1





