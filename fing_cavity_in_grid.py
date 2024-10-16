



def cavityMap(n, grid):
    for i in range(0,n):
        for j in range(0,n):
            if i-1<0 or j-1<0 or j+1==n or i+1==n:
                print(arr[i][j],end="")
            elif (max(arr[i-1][j], arr[i][j-1],arr[i+1][j], arr[i][j+1])<arr[i][j]):
                print("X",end="")
            else:
                print(arr[i][j],end="")
    print("")

n = 4
grid = ['1112', '1912', '1892', '1234']
print(cavityMap(4,[['1112'], ['1912'], ['1892'], ['1234']] ))

