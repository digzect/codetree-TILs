n =  int(input().strip())

dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1

if n == 1 : 
    print(1)
else:
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n])