str1 = input('Введите 1 строку ')
str2 = input('Введите 2 сторку ')

def anagram(str1, str2):
    return sorted(str1) == sorted(str2)

if anagram(str1, str2):
   result=True
else:
   result=False

print (result)