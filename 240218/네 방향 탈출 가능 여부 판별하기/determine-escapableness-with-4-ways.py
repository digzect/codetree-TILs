n, m = map(int, input().split())

array_2D = []
for _ in range(n):
    array_2D.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]


from collections import deque 






#아직 방문하지 않았고, 갈수있는길(1)
def can_go(y,x): 
    if visited[y][x] == False and array_2D[y][x] == 1 : 
        return True 
    return False 


#격자 밖을 벗어나지 않는 
def in_range(y,x):
    if 0<=y<n and 0<=x<m :
            return True 
    return False 






def bfs(yy,xx):
    Q = deque()
    Q.append([yy,xx])

    moves = [(-1,0), (0,1), (1,0), (0,-1)]

    while Q : 
        
        y,x = Q.popleft()


        for d in range(4) :
            dy = y + moves[d][0]
            dx = x + moves[d][1]

            if in_range(dy,dx) and can_go(dy,dx):


                visited[dy][dx] = True 
                # print(dy,dx)
                Q.append([dy,dx])





# print(0,0)
visited[0][0] = True 
bfs(0,0)



if visited[n-1][m-1] == True:
    print("1")
else : 
    print("0")