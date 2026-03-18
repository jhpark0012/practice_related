import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # dp[i] = arr[i]를 마지막으로 하는 LIS 길이

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 10 70 20 30 20 50
