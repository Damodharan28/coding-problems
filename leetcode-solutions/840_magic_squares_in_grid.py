class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(center_row, center_col):
            used_numbers = [False] * 10
            row_sums = [0] * 3
            col_sums = [0] * 3

            for i in range(center_row - 1, center_row + 2):
                for j in range(center_col - 1, center_col + 2):
                    num = grid[i][j]
                    if num < 1 or num > 9:
                        return False
                    row_sums[i - center_row + 1] += num
                    col_sums[j - center_col + 1] += num
                    if used_numbers[num]:
                        return False
                    used_numbers[num] = True

            for used in used_numbers[1:]:
                if not used:
                    return False

            for row_sum in row_sums:
                if row_sum != 15:
                    return False
            for col_sum in col_sums:
                if col_sum != 15:
                    return False

            return (grid[center_row - 1][center_col - 1] + grid[center_row + 1][center_col + 1] == 10 and
                    grid[center_row + 1][center_col - 1] + grid[center_row - 1][center_col + 1] == 10)

        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        magic_square_count = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 5 and isMagic(i, j):
                    magic_square_count += 1
        return magic_square_count
