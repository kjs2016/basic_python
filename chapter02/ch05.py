#실습 문제
print("{:-^20}".format("실습문제"))
a = int(input("정수 a입력 : "))
b = int(input("정수 b 입력 : "))
result = a + b
print("{} + {} = {}".format(a, b, result))

name = input("성명 입력>> ")
language = int(input("국어성적 입력>> "))
english = int(input("국어성적 입력>> "))
math = int(input("국어성적 입력>> "))
total = language + english + math
average = total/3
print('국어 :', language)
print("총점 : {}".format(total))
print("평균 : {}".format(average))