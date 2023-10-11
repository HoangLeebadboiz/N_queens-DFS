import numpy as np


class Board:
    def __init__(self, n):
        self.N = n
        self.position = np.zeros((n, n), dtype=int)
        # self.n_queens = np.zeros((n, 2), dtype= int)
        # self.n_queens = n_queens

    def Draw_board(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.position[i, j] == 0:
                    print('|', end=' ')
                else:
                    print('|', end='X')
            print('|')

    def put_queen(self, n_queens: np.array):
        # self.position[x, y] = 1
        for x, y in n_queens:
            self.position[x, y] = 1


class DFS:
    def __init__(self, n):
        self.N = n
        self.node = []
        self.Board = np.zeros((n, n), dtype=int)
        # self.Back_Board = np.zeros((n, n), dtype= int)
        self.queen = 0
        self.count = 0

    def check(self, position: list):
        # Khởi tạo thông số
        x = position[0]
        y = position[1]
        # queen = 0
        # Xây dựng mô hình
        if len(self.node) == self.N:
            return True
        elif self.Board[x, y] != 0:
            if y >= self.N:
                x = self.node[len(self.node)-1][0]
                y = self.node[len(self.node)-1][1]
                self.backtracking([x, y])

                self.node.pop(-1)

                self.check([x, y+1])
            else:
                self.check([x, y+1])
        else:
            self.node.append([x, y])
            self.Board[x, y] = x
            self.loaitru([x, y])
            self.check([x+1, 0])

    def loaitru(self, position: list):
        x = position[0]
        y = position[1]
        # self.Back_Board = self.Board.copy()
        for i in range(x, self.N):
            for j in range(self.N):
                if (self.Board[i, j] != 0):
                    continue
                elif (i == x and j != y) or (j == y and i != x) or (i + j == x + y) or (i - j == x - y):
                    self.Board[i, j] = -x
                else:
                    continue

        # print(self.Board)

    def backtracking(self, n_position: list):
        x = n_position[0]
        y = n_position[1]
        for i in range(x, self.N):
            for j in range(self.N):
                if i == x and j == y:
                    self.Board = -(x-1)
                if self.Board[i, j] == -x:
                    self.Board[i, j] = 0
                else:
                    continue


n = int(input("Nhap n: "))
solution = DFS(n)
solution.check([0, 0])
# print(solution.node)
# print(solution.node)
n_queens_positions = np.array(solution.node)
board = Board(n)
board.put_queen(n_queens_positions)
board.Draw_board()
print(solution.count)
