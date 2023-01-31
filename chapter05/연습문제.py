list = [] #빈리스트 선언
list2 = [] #빈리스트 선언
for i in range(10) :
    a = int(input("입력 >> "))
    if(a <= 0):
        list.append(a)
    else:
        list2.append(a)

print("양수 리스트 >> ", list2)
print("음수 리스트 >> ", list)

