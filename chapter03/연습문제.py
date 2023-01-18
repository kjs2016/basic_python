# 참조형은 객체를 참조
# 파이썬은 기본적으로 함수형 프로그램이지만 클래스와 객체를 지원한다
# 참조형은  특정 메모리에 있는 객체의 위치를 참조하는 방식으로 데이터를 다룸 -> 객체.맴버의 형식
# 변수 = 객체.멤버속성
# 변수 = 객체.멤버함수()

print(type(365))
print(type('hello'))
print(type(True))
print(type([1,2,4,5]))
print({'no':1, 'name':'kim'})
print(type(print))
print(type(None)) #None -> 0과는 다르다
#print('안녕' + 123) -> 정수와 문자열을 + 연산자로 연결 할 수 없음
print('안녕 ' + str(123))

print("Hello" + " world")
print("Hello~"*5)

print("{:-^20}".format("슬라이싱"))
str1 = 'Hello Python world'
print(str1[6])
print(str1[6:]) #6번째 부터 끝까지 가져오기
print(str1[:6]) #시작점 부터 6번째 까지 가져오기
print(str1[-5])
print("----------------------")

str2 = "Hello world!"
idx = str2.index("world!")
str2 = str2[:idx] + "Python " + str2[idx:]
print(str2)

#문자열 format() 함수를 이용해서 가운데 정렬되도록 소스 코드 작성
print("{:-^50}".format(" 사랑 "))

#데이터를 입력하고 입력된 데이터를 진법 변환하여 그 결과를 2진수, 8진수, 16진수로 출력하는 프로그램을 작성하시오
Int = int(input('정수 입력>>'))
print('2진수로 변환 =>', bin(Int))
print('8진수로 변환 =>', oct(Int))
print('16진수로 변환 =>',hex(Int))

#"Hello python world"를 입력받아서 "Python" 대신 "happy"로 바꿔주는 프로그램을 구현하시오
str3 = input("문자열 입력>> ")
find = str(input("찾을 단어>> "))
#change = input("바꿀 단어>> ")

idx2 = str3.index(len(find))
str3 = str3[:idx] + "python" + str3[idx:]
print(str3)