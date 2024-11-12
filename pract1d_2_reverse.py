def reverse_number(number):
    reverse = 0
    while number > 0:
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number //= 10
    return reverse

number = int(input("Please enter any number: "))
reversed_number = reverse_number(number)
print("\nReversed of entered number is = %d" % reversed_number)
