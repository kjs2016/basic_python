def get_max(num1, num2) :
    if num1 > num2 :
        maxinum = num1
    else :
        maxinum = num2
    return maxinum

result = get_max(10, 100)#함수 호출 후 반환값을 result에 저장
print("더 큰수는 {}입니다!".format(result))
