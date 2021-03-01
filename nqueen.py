#! /usr/bin/env python
# elitehuitzil@gmail.com


# just run in terminal and type number of queens you want to solve :)
	

print ("Enter the number of queens")
N = int(input())


class Queens:

    def __init__(self, n=N):
        self.n = n
        self.reset()
        self.board = [[0]*self.n for _ in range(self.n)]
        self.solutions = []

    def update_board(self, x, y, value):
        self.board[x][y] = value

    def reset(self):
        n = self.n
        self.y = [None] * n
        self.row = [0] * n
        self.up = [0] * (2*n-1)
        self.down = [0] * (2*n-1) 
        self.nfound = 0

    def solve(self, x=0):  
        for y in range(self.n):
            if self.safe(x, y):
                self.place(x, y)
                if x+1 == self.n:
                    self.display()
                else:
                    self.solve(x+1)
                self.remove(x, y)

    def safe(self, x, y):
        return not self.row[y] and not self.up[x-y] and not self.down[x+y]

    def place(self, x, y):
        self.y[x] = y
        self.row[y] = 1
        self.up[x-y] = 1
        self.down[x+y] = 1

    def remove(self, x, y):
        self.y[x] = None
        self.row[y] = 0
        self.up[x-y] = 0
        self.down[x+y] = 0

    def display(self):
        self.nfound = self.nfound + 1
        for idy, y in enumerate(range(self.n-1, -1, -1)):
            for idx, x in enumerate(range(self.n)):
                if self.y[x] == y:
                    self.update_board(idx, idy, 1)
                else:
                    self.update_board(idx, idy, 0)
        print("Solution ", self.nfound)
        for i in self.board:
            print(i)
        print("---" * self.n)
def main():
    n = N
    
    q = Queens(n)
    q.solve()
    print('For %s queens, we have %s solutions.' % (n, q.nfound))
    

if __name__ == "__main__":
    main()
