import sys
from collections import deque

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        p = input().rstrip()
        n = int(input())
        arr_str = input().rstrip()

        # 1) 입력 파싱
        if n:
            arr = deque(map(int, arr_str[1:-1].split(',')))
        else:
            arr = deque()

        rev = False  # 역순 여부 플래그
        error = False

        # 2) 명령 처리
        for cmd in p:
            if cmd == 'R':
                rev = not rev
            else:  # D
                if not arr:
                    print("error")
                    error = True
                    break
                if rev:
                    arr.pop()
                else:
                    arr.popleft()

        if error:
            continue

        # 3) 최종 출력
        if rev:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")

if __name__ == '__main__':
    solve()
