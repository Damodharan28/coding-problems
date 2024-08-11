class Solution:
    def __init__(self):
        self.my_grid = []
        self.visited = set()

    def floodfill(self, r, c, color):
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            if (x, y) in self.visited:
                continue
            self.visited.add((x, y))
            if x < 0 or x >= len(self.my_grid) or y < 0 or y >= len(self.my_grid[0]) or self.my_grid[x][y] != -1:
                continue
            self.my_grid[x][y] = color
            # Check all 4 directions
            stack.append((x - 1, y))
            stack.append((x + 1, y))
            stack.append((x, y - 1))
            stack.append((x, y + 1))

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        max_color = 0

        # Initialize the grid with 0's and -1's based on slashes
        self.my_grid = [[0 for _ in range(n * 3)] for _ in range(n * 3)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    self.my_grid[i * 3 + 0][j * 3 + 2] = -1
                    self.my_grid[i * 3 + 1][j * 3 + 1] = -1
                    self.my_grid[i * 3 + 2][j * 3 + 0] = -1
                elif grid[i][j] == "\\":
                    self.my_grid[i * 3 + 0][j * 3 + 0] = -1
                    self.my_grid[i * 3 + 1][j * 3 + 1] = -1
                    self.my_grid[i * 3 + 2][j * 3 + 2] = -1

        # Count distinct regions
        for i in range(n * 3):
            for j in range(n * 3):
                if self.my_grid[i][j] == -1 and (i, j) not in self.visited:
                    max_color += 1
                    self.floodfill(i, j, max_color)

        return max_color

