#그냥 단순히 1부터 n 까지, 혹은 n부터 1까지 하면 메모리가 터지는 경험을 했음
# DP + BFS 를 섞어서 해결하면 되지 않을까 싶은데...


n = int(input().strip()) 
array = [1111111 for _ in range(n+1)]
array[0] = 0 
array[1] = 1



#array 는 해당 숫자를 만들기에 필요한 연산의 횟수
for i in range(1,n):
    # print(i)
    #2를 넘지 않는경우
    if i*2 < n+1 : 
        array[i*2] = min(array[i*2], array[i]+1)
    
    if i*3 < n+1 : 
        array[i*3] = min(array[i*3], array[i]+1)

    array[i+1] = min(array[i+1], array[i]+1)
    array[i-1] = min(array[i-1], array[i]+1)


    # print(array)
print(array[-1] -1)