# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 구하시오
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

#별찍는 프로그램
i = 0
while True:
 i += 1
 if i > 5: break
 print("{}".format("*") * i)

 #for문을 사용해 1부터 100까지의 숫자를 출력
 for i in range(i, 101):
     print(i)