import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

res = 0
prefix_sum = 0
for i in range(len(arr)-1, 0, -1):
    prefix_sum += arr[i]
    res += arr[i-1] * prefix_sum
    
print(res)