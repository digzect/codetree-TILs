from collections import deque 


n = int(input().strip())


#케이스1. 순서를 위에서부터 아래로 줄여나간다
# def bfs(n):
#     Q = deque()
#     Q.append([n,0])

#     while Q:
#         now, num = Q.popleft()

#         if now == 1 : 
#             return num


#         Q.append([now+1, num+1])
#         Q.append([now-1, num+1])

#         if now%2 == 0: 
#             Q.append([now//2, num+1])
        
#         if now%3 == 0:
#             Q.append([now//3, num+1])


#케이스2. 순서를 1에서부터 위로 늘려나간다.
def bfs(n):
    Q = deque()
    Q.append([1,0])

    while Q:
        now, num = Q.popleft()

        if now == n :
            return num 
        if now == 0:
            continue
        
        Q.append([now+1, num+1])
        Q.append([now-1, num+1])
        Q.append([now*2, num+1])
        Q.append([now*3, num+1])







result = bfs(n)
print(result)