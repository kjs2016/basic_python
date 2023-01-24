li2 = [9,1,8,6,4,3,7,2]
li2.sort()#정렬
print(li2)
li2.reverse()#내용의 위치를 뒤바꾼다
print(li2)

#같은 값의 요소를 한꺼번에 제거
li4 =[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,]
li4.remove(2)#맨 처음에 요소 하나만 제거
print(li4)

while 2 in li4:#li4안에 2가 있다면 반복, 반복할 때마다 remove()함수 요소 제거
    li4.remove(2)플
print(li4)