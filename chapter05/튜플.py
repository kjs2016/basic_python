#튜플 -> List 구조에 비해 실행속도 빠름, 직접 수정 불가능
tup01 = (100, 200, 300, "오징어", "꼴뚜기","대구","명태")#튜플 구조 선언

i = 0
while i<len(tup01) :
    print(tup01[i], end=" ")
    i += 1

