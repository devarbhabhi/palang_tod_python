def is_vowel(char):
    vowels=('a','e','i','o','u')
    if char in vowels:
        return True
    return False
c=input("enter char \n")
print(is_vowel(c))
