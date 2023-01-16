print("Hello" + " world!") #문자열과 문자열을 연결할 때는 +
print("Hello~" * 10)#문자열 반복할때는 *

#[]안에 첨자와 콜론(:)을 이용하여 인덱싱 및 술라이싱

str1 = 'Hello python world'
print(str1[6]) #문자열의 6번째 인덱스의 문자를 출력
print(str1[6:])#6번째 문자열부터 문자열 끝까지 슬라이싱
print(str1[:6])#처음부터 6번째 인덱스까지 슬라이싱
print(str1[-5])#문자열의 끝에서 5번째 인덱스의 문자를 출력