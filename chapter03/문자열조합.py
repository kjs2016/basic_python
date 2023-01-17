str2 = "Hello world"
idx = str2.index("world") #"world"단어가 시작하는 인덱스 위치를 찾아서 idx 변수의 임시 저장
print(str2[:idx])#문자열의 첫번째 부터 world단어 시작부분까지 슬라이싱
print(str2[idx:])#world단어가 시작하는 부분부터 끝까지 슬라이싱

str2 = str2[:idx] + "Python " + str2[idx:]
print(str2)

print(str2[2:-3])
#format 함수()를 이용한 문자열 처리
print("{:-^50}".format("사랑"))
print("{:&<50}".format("사랑"))
print("{:*>50}".format("사랑"))

name = "홍길동"
age = 45
info = "성명:{0} | 나이:{1}".format(name, age) #format함수로 문자열을 조합하고 info변수에 대입
print(info)#info변수의 문자열 값 콘솔 출력

#format함수를 이용한 여러 행 문자열 처리
multiline = '''여러행의 문자열
우리나라는 {}이다.
서기 {}년{}월{}일'''.format("대한민국",2018,4,15)
print(multiline)