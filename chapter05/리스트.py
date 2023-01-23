movieList = ["시네마천국","삼국지","혹성탈출","너의이름은","기생충"]#리스트 선언 및 초기화
print("0. 리스트의 내용 : ", movieList)#moviList 내용 출력
print("1. 리스트의 첫번째 요소 : ", movieList[0])
print("2. 리스트의 마지막 요소 : ", movieList[len(movieList)-1])

movieList[1] = "아이언맨"
print("3. 변경된 리스트의 구조 : ", movieList)#"삼국지"가, "아이언맨"으로 변경돔

del movieList[2]#두 번째 요소 삭제
print("4. 제거후 리스트의 구조 : ", movieList)

movieList.append("분노의 질주")#맨 뒤에 새요소 추가
print("5. 새 요소 추가 : ", movieList)

movieList.insert(2, "슬램 덩크")#2번째 자리에 요소 추가
print("5. 중간에 새 요소 추가 : ", movieList)

print("7. 요소 위치 확인 : ", movieList.index("아이언맨"))#리스트에서 요소의 위치 확인

#append -> 맨마지막에 요소 추가
#insert -> 특정위치에 요소 추가
#del -> 요소 삭제