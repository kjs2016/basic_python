#딕셔너리는 '사전' 이라는 뜻
#{키, 값} 구조
#자바에서는 Map 구조와 비슷함
# 변수이름 dict로 사용 하지 말아야됨

dic = {"name":"홍길동", "phone":"010-4607-8751", "addr":"서울시 종로구 견자동"}

name = dic.get("name")#값을 키로 접근함, get()함수 이용
phone = dic.get("phone")
addr = dic.get("addr")

print("Name : {}".format(name))
print("phone: {}".format(phone))
print("addr : {}".format(addr))
