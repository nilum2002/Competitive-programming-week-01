## This  is based on dynamic programming concepts

## reference the pdf I have Included 



def num_of_ways(N):
    if N <= 1:
        return 0
    
    path_arr = [0]*(N+1) #the starting point is zero
    path_arr[0] = 1
    if N>= 2:
        path_arr[2] = 1
    if N>= 3:
        path_arr[3] = 1
    # start from the 4th 
    for i in range(4, N+1):
        path_arr[i] = path_arr[i-2] + path_arr[i-3]
    return path_arr[N]

N = int(input())
print(num_of_ways(N))



## using recursion 

def num_of_ways_recursive(n):
    if n == 2 :
        return 1
    if n == 3:
        return 1
    if n <= 1:
        return 0
    return num_of_ways_recursive(n-2) + num_of_ways_recursive(n-3)
    pass




n = int(input())

print(num_of_ways_recursive(n))





