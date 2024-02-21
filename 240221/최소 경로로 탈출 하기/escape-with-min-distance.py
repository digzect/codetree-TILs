from collections import deque 

n, m = map(int, input().split())
array_2D = []
for _ in range(n):
    array_2D.append(list(map(int, input().split())))

visited = [[-1 for _ in range(m)] for _ in range(n)]
#갱신을 visited 값 여부로 처맇가ㅣ



#맵 안에 있고, 아직 방문 안한곳 
def can_go(y,x):
    if 0<=y<n and 0<=x<m :
        if array_2D[y][x] == 1 : 
            if visited[y][x] == (-1) :
                return True

    return False 




def bfs():
    Q = deque()
    Q.append([0,0,0])

    moves = [(-1,0), (0,1), (1,0), (0,-1)]


    while Q: 
        y,x,num = Q.popleft()

        for d in range(4):
            dy = y + moves[d][0]
            dx = x + moves[d][1]

            if can_go(dy,dx): 
                # print(dy,dx,num+1)
                visited[dy][dx] = num +1 
                Q.append([dy,dx,num+1])






visited[0][0] = 0
bfs()

print(visited[n-1][m-1])