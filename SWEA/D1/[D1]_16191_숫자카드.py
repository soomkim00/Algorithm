T = int(input())

for t in range(T):
    N = int(input())

    # 입력받은 숫자를 하나씩 탐색하기 위해 리스트로 만들기
    # 빈 리스트에 10으로 나눈 나머지(끝자리 숫자)를 넣고
    # 숫자를 10으로 나눈 몫으로 최신화 : 끝자리 날아감
    number = int(input())
    num_list = []
    for _ in range(N):
        num_list.append(number % 10)
        number //= 10

    # 각 숫자 등장 횟수 체크
    # 0~9를 저장할 크기가 10인 리스트
    # 숫자값을 인덱스로 가지는 리스트의 값 1 증가
    num_count = [0] * 10
    for i in range(len(num_list)):
        num_count[num_list[i]] += 1

    # 최빈수 찾기
    # 최댓값과 0 초기화 후 최댓값보다 크거나 같으면
    # 최댓값 최신화, 인덱스 기록
    # 인덱스 == 최대값을 가진 숫자
    # < 가 아니라 <=인 이유 : 같은 횟수를 가진 수 중 큰 숫자 출력을 위해
    max_num = 0
    max_num_idx = 0
    for i in range(10):
        if max_num <= num_count[i]:
            max_num = num_count[i]
            max_num_idx = i

    print(f'#{t + 1} {max_num_idx} {max_num}')
