#숫자인 인수를 전달받아 출력하는 함수
def show_number(num):
    print("[1] 함수로 전달된 숫자는 ", num ,"입니다.", sep="")

show_number(5)#매개변수가 있는 함수는 호출할 때 반드시 인수를 넣어줘야 된다.

def ge_max(num1, num2):
    if(num1 > num2):
        maxinum = num1

    else:
        maxinum = num2
    return maxinum

result = ge_max(10, 20)
print("더 큰수는", result, "입니다.")