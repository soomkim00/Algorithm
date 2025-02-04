while True:
    lenght_list = list(map(int, input().split()))
    lenght_list.sort()
    if sum(lenght_list) == 0:
        break
    elif lenght_list[2] ** 2 == lenght_list[0] ** 2 + lenght_list[1] ** 2:
        print("right")
    else:
        print("wrong")

# while True 무한 반복
#   why? 종료 조건이 나중에 결정됨
# 입력 값을 리스트로
#   why? 큰 값을 골라내기 위해(정렬) c^2 = a^2 + b^2
# .sort()로 정렬
# 리스트의 합이 0이면 종료
#   why? 입력 조건이 양의 정수, 즉 0 0 0 인 경우만 합이 0
# 정렬된 리스트 인덱싱으로 큰 값 골라서 공식 대입 후 판단
