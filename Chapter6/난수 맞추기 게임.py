import random

number = 0
min = 1  # 전역변수
max = 100  # 전역변수
count = 5  # 사용자가 시도할 수 있는 기회 5번으로 초기화, 전역변수

def check():
    global count
    global min
    global max
    print('정답을 맞출 수 있는 기회는 %d 입니다.' %count)
    user_num = 0
    while user_num < min or user_num > max :
        print("정답은 %d~%d사이입니다" %(min, max))
        user_num = int(input('시스템이 발생 시킨 난수 값은 무엇일까요? >> '))

    if number == user_num :
        print("정답입니다.")
        return True

    else :
        if user_num > number :
            max = user_num -1
            print('크다!')
        else :
            min = user_num + 1
            print('작다!')

    count-= 1;
    return False

def game() :
    print('::::높다 낮다 게임 시작::::')
    global min
    global max
    global count;
    min = 1
    max = 100
    number = random.randint(min, max)#1~100 까지 난수 발생
    print("컴퓨터가 %d부터 %d사이의 난수를 발생 시켰습니다.(Hint:%d)" % (min, max, number))

    while count > 0:
        if check() :
            break

    if count == 0: #카운트 값이 0이면
        print("기회가 소진되어 실격되셨습니다.")

if __name__ == '__main__':
   while True:
       game()
       isPlay = input("다시 시도는 y입력 >> ")
       if isPlay != 'y':
           print("수고요~");
           break
       print('\n다시 시작! 모든 변수를 새로운 값으로 초기화 했습니다.')

