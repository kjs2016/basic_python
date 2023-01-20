str3 = input("문자열 입력>> ")
find = str(input("찾을 단어>> "))
change = input("바꿀 단어>> ")

idx = str3.index(find)
print(str3[:idx])
