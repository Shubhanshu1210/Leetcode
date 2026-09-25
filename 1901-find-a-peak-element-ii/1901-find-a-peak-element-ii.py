class Solution:
    def Intmax(self, mat, n, m, col):
        maxvalue = -1
        index = -1
        for i in range(n):
            if mat[i][col] > maxvalue:
                maxvalue = mat[i][col]
                index = i
        return index

    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while low <= high:
            mid = (low + high) // 2
            maxrowindex = self.Intmax(mat, n, m, mid)
            left = mat[maxrowindex][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxrowindex][mid + 1] if mid + 1 < m else -1
            if mat[maxrowindex][mid] > left and mat[maxrowindex][mid] > right:
                return [maxrowindex, mid]
            elif mat[maxrowindex][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
