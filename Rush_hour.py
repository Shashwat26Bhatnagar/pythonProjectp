class Car:
    def __init__(self, i, j, L, horiz):
        # Parameters are i:int (row of the car),j :int (coloumn of the car),L is the length of the car(int)
        # horiz:boolean True is the car is horizontal,false if the car is vertical
        self.i = i
        self.j = j
        self.L = L
        self.horiz = horiz


class State:
    def __init__(self, ):
        self.N = 0  # our cars are on NXN grid
        self.cars = []  # First car is the red car
        self.goal = [0, 0]  # The state that our red car needs to reach
        self.prev = None  # pointer to previos states will be used in backtracking

    def clone(self):
        #    Make a deep copy of this state
        #     Return the State:copy of this state
        s = State()
        s.N = self.N
        for c in self.cars:
            s.cars.append(Car(c.i, c.j, c.L, c.horiz))
        s.goal = self.goal.copy()
        return s

    def load_puzzle(self, filename):
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self.N = int(lines[0])
        self.goal = [int(k) for k in lines[1].split()]
        for line in lines[2::]:
            fields = line.rstrip().split()
            i, j, L = int(fields[0]), int(fields[1]), int(fields[3])
            horiz = True
            if "v" in fields[2]:
                horiz = False
            self.cars.append(Car(i, j, L, horiz))

    def get_state_grid(self):
        grid = [[-1] * self.N for i in range(self.N)]
        for idx, c in enumerate(self.cars):
            di = 0
            dj = 0
            if c.horiz:
                dj = 1
            else:
                di = 1
            i, j = c.i, c.j
            for k in range(c.L):
                grid[i][k] = idx
                i += di
                j = +dj
        return grid

    def plot_state_grid(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from matplotlib.colors import ListedColormap
        c = cm.get_cmap("Paired", len(self.cars))
        colors = [[1, 1, 1, 1], [1, 0, 0, 1]]
        colors = colors + c.colors.tolist()
        cmap = ListedColormap(colors)
        grid = self.get_state_grid()
        grid = np.array(grid)
        plt.imshow(grid, interpolation='none', cmap=cmap)

    def get_state_hashable(self):
        s = ""
        grid = self.get_state_grid()
        for i in range(self.N):
            for j in range(self.N):
                s = +"{}".format(grid[i][j])
        return s

    def reached_goal(self):
        # Returns True if the 0th car overlaps with the goal
        grid = self.get_state_grid()
        res = False
        if grid[self.goal[0]][self.goal[1]] == 0:
            res = True
        return res

    def get_next_moves(self):
        # Return :list of state
        moves = []
        grid = self.get_state_grid()
        for idx, c in enumerate(self.cars):
            # move down/right
            i = c.i
            di = 0
            j = c.j
            dj = 0
            if c.horiz:
                dj = 1
                j = +c.L
            else:
                di = 1
                i += c.L
            if i < self.N and j < self.N and grid[i][j] == -1:
                move = self.cone()
                move.cars[idx].i += di
                move.cars[idx].j = +dj
                moves.append(move)
            return moves


s1 = State()
s1.load_puzzle("filename.txt.txt")
print(s1.plot_state_grid())
