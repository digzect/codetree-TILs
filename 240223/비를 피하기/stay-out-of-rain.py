# 크기 n * n. 
# 사람 h 명 
# 비를 피할수 있는 공간의 위치 m 

# 0: 해당 칸이 이동할수 있는곳이다
# 1: 벽이 있어서 이동할수 없는곳이다
# 2: 해당 칸에 사람이 서있다.
# 3: 해당공간이 비를 피할수 있는 공간이다

# 이동: 상하좌우, 1초
# 벽이아닌곳은 이동이 가능하다.

#컨셉: 
#사람이 있는 좌표를 처음에 입력받는다 -> 리스트로 따로 만들어둔다
#각 사람마다 bfs 를 돌아서 최소 거리를 리턴받아서 결과로 내보낸다 
#맨 처음 사방이 막혀있는지를 판단해서 -1 을 리턴한다.

#특이사항
#h명이 있는지 없는지는 크게 신경쓸 부분이 아니다.
#방문처리: 각각 유저에 대한 bfs 를 진행할거라서 ... 한명 시작할때마다 방문여부맵을 만든다

#복잡도
#BFS를 n^n에 대해서 진행하는게 아니라 주어진 데이터에 대해서만 진행하니까 최소면 뭐...O(1)일거고, 최악이면 O(n)까지 가겠지


from collections import deque 

n,h,m = map(int, input().split())
array_2D = []
human = []
result =[[0 for _ in range(n)] for _ in range(n)]


for nn in range(n):
    lis = list(map(int, input().split()))
    # print(lis)

    for li in range(n):
        if lis[li] == 2 : 
            human.append([nn,li])
    array_2D.append(lis)







def bfs(yy,xx):

    visited = [[False for _ in range(n)] for _ in range(n)]

    Q = deque()
    Q.append([yy,xx,0])
    visited[yy][xx] = True 
    
    moves = [(-1,0), (0,1), (1,0), (0,-1)]



    while Q :
        y,x,num = Q.popleft()
        
        for d in range(4):
            dy = y + moves[d][0]
            dx = x + moves[d][1]

            
            #사방을 벗어나지 않고
            if 0<=dy<n and 0<=dx<n : 

                #아직 가본곳이 아니고
                if visited[dy][dx]== False :

                    #갈수 있는곳 이면 (벽이 아니면 )
                    if array_2D[dy][dx] != 1 :

                        #종료조건
                        if array_2D[dy][dx] == 3 :
                            return num+1

                        #종료하지못하는조건 
                        #방문처리, num추가
                        visited[dy][dx] = True 
                        Q.append([dy,dx,num+1])

    #비를피할곳까지 못도착하는 경우 
    return -1



#모든 human에 대해서
for huma in human :
    yy, xx = huma
    res = bfs(yy,xx)    
    result[yy][xx] = res 

# print("\n")

#값 결과 출력하기
for resul in result:
    for resu in resul :
        print(resu, end=' ')
    print()