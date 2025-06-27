import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    M = int(input())
    S = input().strip()

    cnt = 0    # 연속된 "IOI" 패턴 수
    ans = 0    # 최종 정답
    i = 0
    # i < M-2 인 이유: i, i+1, i+2 접근을 위해
    while i < M - 2:
        if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
            cnt += 1
            # cnt가 N에 딱 도달하면 한 번 추가, 이후 겹치게 세기 위해 cnt-- 해 줌
            if cnt == N:
                ans += 1
                cnt -= 1
            i += 2
        else:
            cnt = 0
            i += 1

    print(ans) 

if __name__ == '__main__':
    solve()