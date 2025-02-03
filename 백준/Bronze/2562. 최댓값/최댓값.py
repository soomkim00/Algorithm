number_list = []
for _ in range(9):
    number_list.append(int(input()))

# 리스트 최대값 구하는 내장 메서드
print(max(number_list))

# 리스트 인덱스 구하는 리스트 메서드
# 인덱스는 0부터 시작이라서 + 1
print(number_list.index(max(number_list)) + 1)
