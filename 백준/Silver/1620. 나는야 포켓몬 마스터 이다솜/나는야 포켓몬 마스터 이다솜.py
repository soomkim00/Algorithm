import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    pokemons = [input().strip() for _ in range(N)]
    for _ in range(M):
        questioin = input().strip()
        if questioin.isdecimal():
            print(pokemons[int(questioin) - 1])
        else:
            print(pokemons.index(questioin) + 1)


if __name__ == "__main__":
    solve()
