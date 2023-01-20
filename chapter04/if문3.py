import sys

name = input("성명 입력 :")
if len(name) == 0:
    print("성명을 입력하지 않았습니다.")
    sys.exit()#성명이 입력되지 않으면 바로 종료되는 함수

print("당신의 이름은 {}이고, {}글자 입ㄹ니다.".format(name, len(name)))