from collections import deque 

# - 조건을 만족하는 위치로만 이동
# - k번 반복하지 못했지만, 새로이동할 위치가 없다면 종료
# - k번 반복한 이후의 위치

# 조건
# - 시작위치 x 인접한곳에서 x보다 작은곳으로 이동
# -도달할 수 있는 칸들 중 최댓값으로 이동함. 
# -만족하는 숫자가 여러개면, 행 번호가 가장 작은곳으로 이동함 
# - 만족하는 숫자가 여러개고, 행 번호가 낮은곳이 여러개면 ,열번호가 가장 낮은곳으로 이동함 



#필요한 함수
# 1. 시작할때 현재 4위치의 값이, 현재 값보다 큰 값인지 판단하는함수
#     True : 종료
#     False : loop 돌기

# 2. 내가 갈수있는 좌표 중, 가장 숫자가 큰 값의 좌표를 구하는 함수
#     그냥 무식하게 for문 2개돌면서, 현재값보다 비교하는건 큰 의미가 있나 ?
    
#     시간복잡도에서 터지지않을까? n은 최대 100, 그렇다면 n^2 은 10000. 루프한번돌때 10^4 가 걸리는거고, k도 100 까지니까
#     이거 최대로 잡아도 10^6나오겠다. 
#     10^8 이 1초니까 터지진 않을거같음

# 3. 리스트에 있는 좌표 -> 숫자로 받아내서 
#     - 가장 행 번호가 작은 값 이나 
#     - 행 번호가 같다면 , 가장 열 번호가 작은 값으로 비교하는 함수



#visited 는 필요함 

n, k = map(int, input().split())
array_2D = []
for _ in range(n):
    array_2D.append(list(map(int, input().split())))


a,b = map(int, input().split())
start = [a-1, b-1]
# print(f"start is {start}")









#갈수있는 리스트 항목을 정렬하는 함수
def move_located(movable): 
    
    #키를 두개로 해서, 행번호, 열번호 순서로 정렬하는 함수 
    movable.sort(key=lambda x: (x[0], x[1]))
    # print(movable)

    return movable[0]





#움직일수 있으면 True 를 반환하는 함수 
def check_four_side(y,x):

    moves = [(-1,0), (0,1), (1,0), (0,-1)]
    for d in range(4):
        # print(f"y is {y}")
        # print(f"moves[d] is {moves[d]}")
        # print(f"moves[d][0] is {moves[d][0]}")

        dy = y + moves[d][0]
        dx = x + moves[d][1]

        #안에 있고 
        if 0 <= dy < n and 0 <= dx < n : 
            
            #현재 값보다 작은 값이 존재하는는 경우 
            if array_2D[dy][dx] < array_2D[y][x] : 
                # print("check_four_side is true")
                return True             

    #마지막까지 리턴된게없으면, 더이상 움직일 수 없는것임
    # print("check_four_side is false")
    return False 



#bfs를 돌면서, 나보다 작은 값을 리스트에 넣는 함수, 반환을 해야함 
def bfs(num1,num2):


    Q = deque()
    Q.append([num1,num2])



    moves = [(-1,0), (0,1), (1,0), (0,-1)]

    #매번bfs 를 할따마다 필요하기 떄문에 추가.
    visited = [[False for _ in range(n)] for _ in range(n)]

    max_list = []   #가장 큰 값을 가진 좌표 
    max_num = 0     #가장 큰 값

    while Q : 
        y,x = Q.popleft()

        for d in range(4):
            dy = y + moves[d][0]
            dx = x + moves[d][1]

            #조건1. 내부에 있거나
            if 0<=dy<n and 0<=dx<n :

                #조건2. 아직 안들렸거나
                if visited[dy][dx] == False :

                    #조건3. 현재 값보다 작은곳 이여야만 큐에넣음
                    if array_2D[dy][dx] < array_2D[num1][num2] : 

                        #가장 큰 값이라면 
                        if max_num < array_2D[dy][dx] : 
                            max_num = array_2D[dy][dx] 
                            max_list = [[dy,dx]]

                        elif max_num == array_2D[dy][dx] : 
                            max_list.append([dy,dx])
                        
                        else:
                            pass 

                        visited[dy][dx] = True 
                        Q.append([dy,dx])
    return max_list 
    
    






for kk in range(k):


    # print(start)

    #움직일 수 있다면 
    if check_four_side(start[0], start[1]):

        #움직일수 있는 리스트를 반환해야함 
        movable_list = bfs(start[0], start[1])

        #최종적으로 이동하는 한 곳 
        start = move_located(movable_list)


    #움직일수 없다면, 종료한다 
    else:
        break 


#끝난상황 
# print("끝")
print(start[0]+1, start[1]+1)