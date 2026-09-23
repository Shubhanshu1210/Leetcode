class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = 1
        ansroww = []
        ansroww.append(ans)

        for col in range(1, rowIndex + 1):
            ans = ans * (rowIndex - col + 1)
            ans = ans // col
            ansroww.append(ans)

        return ansroww