import random

dlist ={}
count = 5
a_count = 0
w_count = 0

while True:
   print("-----------------")
   print("1. 단어 추가")
   print("2. 단어 삭제")
   print("3. 문제 풀기")
   print("4. 단어장 보기")
   print("5. 단어장 내용 전부 지우기")
   print("6. 종료")
   print("-----------------")
   num = int(input("메뉴 선택 : "))

   if num == 1 :
     print("한번에 5개씩 추가 할 수 있습니다.")
     for i in range(count):
        eng = input("추가할 영어단어를 입력하세요 : ")
        kor = input("한국어 뜻을 입력하세요 : ")
        dlist[eng] = kor
        print("단어를 추가했습니다.")

   if num == 2:
       if dlist == {}:  # 단어장이 비어있을 경우
           print("단어장이 비어 있습니다. 단어를 추가해 주세요.")

       else:
             delete = input("삭제할 단어를 영어로 입력하세요 : ")
             del(dlist[delete])
             print(dlist)#list 요소 출력

   if  num == 3 :
      if dlist == {} :#단어장이 비어있을 경우
            print("단어장이 비어 있습니다. 단어를 추가해 주세요.")
      else :
           key_list = list(dlist.keys())
           for i in range(len(key_list)):
               random_eng =random.sample(key_list)
               result = input("%s의 뜻을 쓰시오 : " %random_eng)
               if dlist.get(random_eng) == result: #키값의 value가 사용자가 입력한 값과 같다면 정답
                   print("정답입니다")
                   a_count += 1
               else:
                   print("정답이 아닙니다.")
                   w_count += 1
      print("맞은 개수 >>{}, 틀린 개수 >>{}".format(a_count, w_count))

   if  num == 4:
       if dlist == {}:  # 단어장이 비어있을 경우
           print("단어장이 비어 있습니다. 단어를 추가해 주세요.")
       else :
           print(list)

   if num == 5:
       print("단어장 내용을 전부 지웁니다.")
       list.clear()

