


matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotateMatrix(matrix)  :
    for i in range(3)              :
     for j in range(i,3):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(3):
     matrix[0][i],matrix[2][i] =matrix[2][i],matrix[0][i]
    return matrix
      
       
a=rotateMatrix(matrix)
print(a)
