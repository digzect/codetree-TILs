from collections import deque 

n = int(input().strip())



def bfs(n):
    Q = deque()
    Q.append([n,0])

    while Q:
        now, num = Q.popleft()

        if now == 1 : 
            return num


        Q.append([now+1, num+1])
        Q.append([now-1, num+1])

        if now%2 == 0: 
            Q.append([now//2, num+1])
        
        if now%3 == 0:
            Q.append([now//3, num+1])






result = bfs(n)
print(result)