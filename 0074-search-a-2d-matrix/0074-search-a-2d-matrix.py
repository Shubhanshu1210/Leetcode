class Solution:
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n * m - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // m][mid % m]
            if val == target: return True
            elif val < target: low = mid + 1
            else: high = mid - 1
        return False