for fish in ["오징어", "꼴뚜기","대구","명태","거북이"] :
    print(fish, end=" ")

print('\n')
#print(type(fish))

total = 0#0으로 초기화
lis = [95, 80, 100, 70, 85];
print("성적", end=":")
for score in lis:
    print(score, end=" ")
    total += score

print("\n총점 :", total)
print("평균 :", total/len(lis))