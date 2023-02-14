# Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.

# Example:

# Input:
# mat[N][N] = {{ 1, 2, -1, -4, -20 },
#              { -8, -3, 4, 2, 1 },
#              { 3, 8, 6, 1, 3 },
#              { -4, -1, 1, 7, -6 },
#              { 0, -4, 10, -5, 1 }};
# Output: 18
# The maximum value is 18 as mat[4][2]
# - mat[1][0] = 18 has maximum difference.


def findMaxDiff(mat):
    n = len(mat)
    m = len(mat[0])
    max = -float("inf")
    for i in range(n):
        for j in range(m):
            ele = mat[i][j]
            if ele > max:
                max = ele
                c,d=i,j
    
    result=-float('inf')

    for i in range(c+1):
        for j in range(d+1):
            ele = mat[i][j]
            diff=int(max-ele)
            if diff>result:
                result=diff 
    print(result)



mat = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]
findMaxDiff(mat)