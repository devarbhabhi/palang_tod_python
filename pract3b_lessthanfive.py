def LessThanFiveChecker(li,n):
    New_li=[ele for ele in li if ele<n]
    return New_li
if __name__=="__main__":
    li=[1,1,2,3,4,8,13,21,34,55,89]
    print("The List is"+str(li))
n=int(input("Enter a Number to return a list that contains only elements from the original list that are smaller than the number:"))
New_li=LessThanFiveChecker(li,n)
print(New_li)
