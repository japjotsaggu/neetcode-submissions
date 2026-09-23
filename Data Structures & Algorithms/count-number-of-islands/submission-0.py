class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        island_counts = 0 
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        island_counts += 1
                        stack = [(i, j)]
                        grid[i][j] = "0"

                        while stack:
                            curr_i, curr_j = stack.pop()
                            for step in steps:
                                i_new, j_new = curr_i+step[0], curr_j+step[1]
                                if 0<=i_new<len(grid) and 0<=j_new<len(grid[0]):
                                    if grid[i_new][j_new] == "1":
                                        grid[i_new][j_new] = "0"
                                        stack.append((i_new,j_new))

        return island_counts
            

                            




        
        