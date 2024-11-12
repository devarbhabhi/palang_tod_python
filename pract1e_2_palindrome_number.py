num = int(input("Enter number: "))
reversed_num = 0
original_num = num 

while num != 0:
    rem = num % 10
    reversed_num = reversed_num * 10 + rem
    num = num // 10

if reversed_num == original_num:
    print(original_num, "is a palindrome!")
else:
    print(original_num, "is not a palindrome!")
