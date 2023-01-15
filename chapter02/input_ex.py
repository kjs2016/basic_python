user_name = input("사용자 이름 입력 : ")
print(user_name,'입니다.')

num1 = int(input("num1 입력 : "))#정수 타입으로 형변환
print(type(num1))

a = int((input("정수 입력 : ")))
b = int(input("정수b 입력 : "))
result = a + b
print("{} + {} = {}".format(a, b, result))

#input함수로 입력받은 데이터는 무조건 문자열 데이터이다. 숫자로 사용하기 위해서는 int(), float() 함수로 형변환 해야 된다.