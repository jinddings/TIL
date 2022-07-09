n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    c.append(int(input()))
    # 동전의 가지 입력

for i in c: #i원의 동전을 사용할 때
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])
