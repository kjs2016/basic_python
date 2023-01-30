import random

def game() :
    print('::::높다 낮다 게임 시작::::')
    min = 1 #전역변수
    max = 100 #전역변수
    count = 5#사용자가 시도할 수 있는 기회 5번으로 초기화, 전역변수
    number = random.randint(min, max)#1~100 까지 난수 발생
    print("컴퓨터가 %d부터 %d사이의 난수를 발생 시켰습니다.(Hint:%d)" % (min, max, number))

    while count > 0:
        print("정답은 %d~%d 사이입니다/." % (min, max))
        user_num = int(input('시스템이 발생 시킨 난수 값은 무엇일까요 >> '))
        count -= 1

    if count == 0: #카운트 값이 0이면
        print("기회가 소진되어 실격되셨습니다.")

if __name__ == '__main__':
   while True:
       game()
       isPlay = input("다시 시도는 y입력 >> ")
       if isPlay != 'y':
           print("수고요~");
           break

