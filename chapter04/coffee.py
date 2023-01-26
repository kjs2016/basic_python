coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 드리겠습니다. 감사합니다")
        coffee = coffee-1
    elif money > 300 :
         result = int(input("1. 거스름돈 받기, 2. 돈 만큼 커피 받기 : "))
         if result == 1 :
            print("커피를 주고 거스름돈을 줍니다 : %d원" % money // 300)
            coffee = coffee -1
         else:
             print("%d개의 커피를 드리겠습니다. 감사합니다." % (money // 300))
             coffee = coffee - (money // 300)
    elif money < 300:
        print("%d원이 부족합니다."%(300-money))
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피는 %d개 입니다."%coffee)
    if coffee == 0:
        print("커피가 하나도 없습니다. 죄송합니다.")
        break
