import datetime
from datetime import date, timedelta

print("어서오세요.")
#성명을 입력받아서 user_name변수에 저장
user_name = input("성명을 입력 하세요>> ")
print("%s님 안녕하세요" %user_name)
birth_year = int(input("생년을 입력 하세요(ex: 1991) >>"))
str_today = str(datetime.date.today())#현재 날짜를 str_today변수에 저장, 연도만 추출하기 위해 문자열 변수로 형변환
now_year = int(str_today.split('-')[0])#현재 연도를 추출해서 now_year변수에 저장, 문자열 데이터를 숫자 연산을 해야되기 때문에 int()함수로 형변환
age = now_year-birth_year#현재 연도에서  생년을 빼면 나이가 나온다.
print("%s님은 %d년 현재 %d세입니다. \n" %(user_name, now_year, age))

if(age < 19):
    print("%s님은 미성년자 입니다." %user_name)#19살 미만일 때 실행
else:
    print("%s님은 성인입니다." %user_name)#19살 미만이 아니라면 실행