memo = {0: [1, 0], 1: [0, 1]}
memo[2] = [memo[0][0] + memo[1][0], memo[0][1] + memo[1][1]]
print(memo[0])