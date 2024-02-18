from collections import deque


n, k = map(int, input().split())
array_2D = []
for _ in range(n):
    array_2D.append(list(map(int, input().split())))
visited = [[False for _ in range(n)] for _ in range(n)]

rc = []
for _ in range(k):
    a,b = map(int,input().split())
    rc.append([a-1, b-1])



#격자를 벗어나지 않는지 
def in_range(y,x):
    if 0<=y<n and 0<=x<n : 
        return True 
    return False 





#갈수있는 숫자(0) 인지 
def can_go(y,x):
    if array_2D[y][x] == 0 : 
        return True 
    return False 




#이미 방문한 곳인지 
def can_visit(y,x):
    if visited[y][x] == False :
        return True 
    return False 







def bfs():
    
    moves = [(-1,0), (0,1), (1,0), (-1,0)]
    global cnt

    while Q : 
        y,x = Q.popleft()

        for d in range(4):
            dy = y + moves[d][0]
            dx = x + moves[d][1]


            if in_range(dy,dx) and can_go(dy,dx) and can_visit(dy,dx) :
                cnt += 1 
                # print(dy,dx)
                visited[dy][dx] = True 
                Q.append([dy,dx])






#큐에 인잇
Q = deque()
for r in rc :
    Q.append(r)

cnt = 0 
bfs()



#결과 
print(cnt)