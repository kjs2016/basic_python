# if문 형식
#if 조건식 :
#   조건식이 참이면 실행

money = True
if money:
    print("택시를 탄다")
else:
    print("걸어간다")
print("{:-^60}".format("-"))
money = 2000
if money >= 3000:
    print("택시를 탄다")
else:
    print("걸어간다")
print("{:-^60}".format("-"))
money = 2000
card = True
if money >= 3000 or card:# -> 둘중 하나만 참이어도 참
    print("택시를 탄다")
else:
    print("걸어간다")
print("{:-^60}".format("-"))
if money >= 3000 and card:#and -> 모두 참일 경우 참
    print("택시를 탄다")
else:
    print("걸어간다")