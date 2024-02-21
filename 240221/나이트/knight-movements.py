from collections import deque 

n = int(input().strip())
r1, c1, r2, c2 = map(int, input().split())
r1 = r1-1
c1 = c1-1
r2 = r2-1
c2 = c2-1


visited = [[-1 for _ in range(n)]for _ in range(n)]



#방문한적 없으면 True 
def can_visit(y,x):
    if visited[y][x] == (-1) :
        return True 
    return False 


#방문가능하면 True 
def in_range(y,x):
    if 0<=y<n and 0<=x<n : 
        return True 
    return False 


def bfs(yy,xx,num):
    Q = deque()
    Q.append([yy,xx,0])

    while Q : 
        y,x,num = Q.popleft()
        moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2),(-1,-2),(-2,-1)]

        for d in range(8):
            dy = y + moves[d][0]
            dx = x + moves[d][1]

            if in_range(dy,dx) and can_visit(dy,dx):
                
                visited[dy][dx] = num+1
                Q.append([dy,dx,num+1])





visited[r1][c1] = 0 
bfs(r1,c1,0)
print(visited[r2][c2])