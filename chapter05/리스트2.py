#리스트 선언
lis = []#빈 리스트 선언. 리스트에 추가되는 각각의 요소 데이터들은 서로 타입이 달라도 문제x

lis.append("홍길동")
lis.append("김길동")
lis.append(100)
lis.append(200)
lis.append(3.14)
print(type(lis))
print(lis)

#리스트 연결
li = ["홍길동, 23"] #리스트 초기화
li.append("서울시 은평구")#맨 마지막에 요소 추가
li += ["aaa", "bbb"]# 새로운 리스트 연결
li.append(["ccc", "ddd"])#중첩 리스트 형태로 리스트 요소에 다른 요소가 추가
print(li)