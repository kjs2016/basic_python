import random

lotto = set()#set 자료 구조는 중복된 값을 허용하지 않는다.

while len(lotto) < 6:
    lotto.add(random.randint(1,45))


print("---로또 번호 생성---")
for i in lotto :
    print(i, end="   ")#번호 사이 간격 조절