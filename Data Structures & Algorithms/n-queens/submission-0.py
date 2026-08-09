class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (c-r) in negDiag or (c+r) in posDiag:
                    continue

                col.add(c)
                posDiag.add(c+r)
                negDiag.add(c-r)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(c+r)
                negDiag.remove(c-r)
                board[r][c] = "."

        backtrack(0)
        return result



        