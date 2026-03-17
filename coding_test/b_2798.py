import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


res = -1
flag = True
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            card_sum = arr[i] + arr[j] + arr[k]
            
            if card_sum <= M:
                res = max(card_sum, res)
print(res)