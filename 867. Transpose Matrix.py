class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [] 
        sizeMat = len(matrix)
        numele = len(matrix[0])
        for i in range(numele) :
            mat.append([])
            for k in range(sizeMat):
                mat[i].append(matrix[k][i])
        return mat