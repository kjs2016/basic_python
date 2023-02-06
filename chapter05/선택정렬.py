arr = [64, 25, 12, 22, 11]

# 배열의 길이만큼 반복문 실행
for i in range(len(arr)):

    # 가장 작은 값을 저장할 변수에 i를 초기화
    min_idx = i
    for j in range(i + 1, len(arr)):
        # 만약 가장 작은 값변수가 다음 인덱스의 값보다 클경우
        if arr[min_idx] > arr[j]:
            min_idx = j # 값을 변경

    # 값을 변경
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 정렬한 배열을 출력
print("[Sorted array]")
for i in range(len(arr)):
    print("%d " %arr[i], end = "")