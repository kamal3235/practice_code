# input
# The first line contains space separated integers N, M  and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.
import numpy as np

N, M, P = map(int, input().split())

arr1 = np.array([input().split() for _ in range(N)], int)
arr2 = np.array([input().split() for _ in range(M)], int)
print(np.concatenate((arr1, arr2), axis=0))




