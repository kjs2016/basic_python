print("::: 나는 65세까지 몇년 남았을까? :::")
user = input("성명 입력 >> ") #사용자로 부터 데이터 입력받아 user변수에 저장
age = int(input("나이 입력 >> "))# 정수로 사용되는 데이터 형변환
futureAge = 65 - age
print("{:-^25}".format("입력 정보 확인"))
print("{}님의 65세까지 {}년 남았습니다.".format(user, futureAge))
print("{:-^28}".format("-"))
