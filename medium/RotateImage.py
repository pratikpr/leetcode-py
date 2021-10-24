from typing import List

'''
https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''
class RotateImage:
    def rotateFourCells(self, matrix: List[List[int]]) -> None:
        for i in matrix:
            s = [str(ints) for ints in i]
            i = " ".join(s)
            print(str(i))
        print()

        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = temp
        for i in matrix:
            s = [str(ints) for ints in i]
            i = " ".join(s)
            print(str(i))
        print()

    def rotateTransposeReflect(self, matrix: List[List[int]]):
        self.transpose(matrix)
        self.reflect(matrix)
        for i in matrix:
            s = [str(ints) for ints in i]
            i = " ".join(s)
            print(str(i))

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

obj = RotateImage()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.rotateFourCells(matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.rotateTransposeReflect(matrix)