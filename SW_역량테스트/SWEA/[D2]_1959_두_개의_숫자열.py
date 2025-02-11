# 길이가 긴 쪽을 기준으로 짧은 문자열이 이동하면서 탐색
# 인덱스가 서로 다름을 주의!

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    result = 0
    if a < b:
        for i in range(b - a + 1):
            temp = 0
            for j in range(a):
                temp += Ai[j] * Bi[j + i]
            if temp > result:
                result = temp
    else:
        for i in range(a - b + 1):
            temp = 0
            for j in range(b):
                temp += Ai[j + i] * Bi[j]
            if temp > result:
                result = temp
    print("#%d %d" % (test_case, result))
