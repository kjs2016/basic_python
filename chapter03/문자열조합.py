str2 = "Hello world"
idx = str2.index("world") #"world"단어가 시작하는 인덱스 위치를 찾아서 idx 변수의 임시 저장
print(str2[:idx])#문자열의 첫번째 부터 world단어 시작부분까지 슬라이싱
print(str2[idx:])#world단어가 시작하는 부분부터 끝까지 슬라이싱

str2 = str2[:idx] + "Python " + str2[idx:]
print(str2)

print(str2[2:-3])