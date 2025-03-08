arr = sorted(eval(input()))
target = int(input())
n  = []
for i in range(len(arr)):
    
    for j in range(len(arr)):
        for k in range(len(arr)):
            for x in range( len(arr)):
                if arr[i] + arr[j] +arr[k] +arr[x] == target:
                    sub = []
                    sub.append(arr[i])
                    sub.append(arr[j])
                    sub.append(arr[k])
                    sub.append(arr[x])
                    
                    n.append(sub)
        
print(n)

# not the optimal solution - Time complexity is O(N^4) - there are 4 for loops