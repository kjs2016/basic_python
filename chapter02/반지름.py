
print("원의 반지름 구하는 프로그램")
redius = int(input("원의 반지름 입력>> "))
pi = 3.14

a = 2 * pi * redius
b = pi * redius * redius

print("반지름이 {} 둘레의 길이는{}이고 넓이는{}입니다.".format(redius, a, b))
