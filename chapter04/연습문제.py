#다음 if문의 조건식을 완성하시오
import sys

print("정수를 입력 하면 양수, 음수, 0을 판별합니다.")
integer = int(input('정수 입력>> '))
if integer > 0 :
    print("양수입니다.")
elif integer < 0 :
    print("음수 입니다.")
else :
    print("0입니다.")

#아래처럼 name 변수에 성명을 입력받고 만약 이름이 입력되지 않으면 "이름이 이름이 입력되지 않으면 "이름이 입력되지 않았습니다"라고
#오류 메시지가 출력되도록 하는 소스 코드를 적으시오


name = input("성명을 입력하세요 :")
if name =="":
   print("이름이 입력되지 않았습니다.")
else:
    print("이름은 %s 입니다." %name)

#정수를 입력받아서 3의 배수를 판별하는 프로그램
integer = int(input("정수를 입력 하세요 : "))
print(integer, ": ", end=" ")

if integer == 0:
    print("0입니다.")

if integer == 5:
    print("5입니다.")

elif integer%3 == 0:
    print("3의 배수 입니다.")

else :
    print("3의 배수가 아닙니다.")

#성적을 입력받아서 학점으로 환산하는 프로그램
score = input("성적 입력 : ")
grade = "F"

if score.isalpha() == True:
   print("Error")
   sys.exit()

else:
    score = int(score)
    if score >= 90:
        grade = 'A'
    elif score >= 80:
         grade = 'B'
    elif score >= 70:
         grade = 'C'
    elif score >= 60:
         grade = 'D'

print("{}점은 {}학점이다.".format(score, grade))