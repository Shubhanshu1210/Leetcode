
class Solution:
    def generaterow(self, row):
        ans = 1
        ansroww = []
        ansroww.append(ans)

        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansroww.append(ans)

        return ansroww

    def generate(self, numRows):
        ans = []

        for i in range(1, numRows + 1):
            ans.append(self.generaterow(i))

        return ans

