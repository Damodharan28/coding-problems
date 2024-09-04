class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y,d = 0,0,0
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        m_dist = 0
        obstacles=set(map(tuple,obstacles))

        for i in commands:
            if i == -1 :
                d = (d+1)%4
            elif i == -2 :
                d = (d-1)%4
            else :
                for _ in range(i):
                    nx,ny = x + direct[d][0], y + direct[d][1]
                    if (nx,ny) in obstacles:
                        break
                    x,y = nx,ny
                    m_dist = max(m_dist, x*x + y*y)

        return m_dist
