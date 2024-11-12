number=int(input("Print Enter any number:"))
reverse=0
while(number>0):
    reminder=number%10
    reverse=(reverse*10)+reminder
    number=number//10
print("\n reverse of entered number is=%d"% reverse)    
