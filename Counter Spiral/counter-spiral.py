#Taking dimensions n x n
n =  int(input())
arr=[]
#Then storing those in 2D List
for i in range(0,n):
    arr.append([int(x) for x in input().split(" ")])
#Taking length to reduce the number for spiral
length = len(arr)
z = 0
k= 0 
i = length
while(i > 0):
    #first for vertical move
    for j in range(z,i):
        print(arr[j][k], end = ' ')
    i = i - 1 
    k = j
    #for turning
    if (i > 0):
        #for horizontal move
        for j in range(length-i, i + 1):
            print(arr[k][j], end = ' ')
        #for vertical move
        for j in range(k-1, length-2-i, -1):
            print(arr[j][k], end = ' ')
    # if i is 0 in if condition before this statement then 
    # break the while loop 
    else:
        break
    k = j
    i = i-1
    if (i > 0): 
        #for horizontal move
        for j in range(i,length-2-i,-1):
            print(arr[k][j], end = ' ')
        k,i = k+1,i+1
        z = z + 1
    # if i is 0 in if condition before this statement then 
    # break the while loop 
    else:
        break
    #then looped to while for one more circle
