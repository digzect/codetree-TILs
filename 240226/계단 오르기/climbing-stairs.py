n = int(input().strip())

dp = [0 for _ in range(n+1)]

if n == 2 : 
    print(1)

elif n == 3 :
    print(1)

else: 
    dp[2] = 1
    dp[3] = 1

    for i in range(2,n+1):
        if i+2 < n+1: 
            dp[i+2] = dp[i] + 1 
        
        if i+3 < n+1:
            dp[i+3] = dp[i] + 1 


    print(dp[n]%10007)