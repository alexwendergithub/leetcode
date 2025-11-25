class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        captures = 0
        for i in range(8):
            for j in range(8):
                if board[i][j]=='R':
                    Ri=i-1
                    #verify top
                    while Ri>=0:
                        if board[Ri][j]!=".":
                            if board[Ri][j] == "p":
                                captures+=1
                            break
                        Ri-=1
                    Ri=i+1
                    #verify down
                    while Ri<8:
                        if board[Ri][j]!=".":
                            if board[Ri][j] == "p":
                                captures+=1
                            break
                        Ri+=1
                    Rj=j-1
                    #verify left
                    while Rj>=0:
                        if board[i][Rj]!=".":
                            if board[i][Rj] == "p":
                                captures+=1
                            break
                        Rj-=1
                    Rj=j+1
                    #verify right
                    while Rj<8:
                        if board[i][Rj]!=".":
                            if board[i][Rj] == "p":
                                captures+=1
                            break
                        Rj+=1
                    return captures
        return -1