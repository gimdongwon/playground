graph = [[], [2,3,8], [1,7], [1,4,5],[3,5],[3,4], [7],[2,6, 8],[1,7]]
visited = [False]*9

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#dfs(graph, 1, visited)

from collections import deque

def bfs(graph, start, visited):
    # queue 구현을 위해 라이브러리 상숑
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# bfs(graph, 1, visited)

def iceAge():
    iceGraph = [[0,0,0,0,0,1,1,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]
    n,m = len(iceGraph), len(iceGraph[0])
    def iceMaker(x,y):
        if x<=-1 or x>=n or y<=-1 or y>=m:
            return False
        if iceGraph[x][y] ==0:
            iceGraph[x][y] = 1
            iceMaker(x-1, y)
            iceMaker(x+1, y)
            iceMaker(x, y-1)
            iceMaker(x, y+1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if iceMaker(i,j) == True:
                result+=1
    print(result)

def maze():
    # mazeGraph = [[1,1,0], [0,1,0],[0,1,1]]
    mazeGraph = [[1,0,1,0,1,0], [1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1], [1,1,1,1,1,1]]
    n,m = len(mazeGraph), len(mazeGraph[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def escape(x,y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()
            # 현재 위치에서 4 방향으로의 위치 확인
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                # 미로 찾기 공간에서 벗어난 경우 무시
                if nx < 0 or nx >= n or ny<0 or ny>=m:
                    continue
                # 벽인 경우 무시
                if mazeGraph[nx][ny] ==0:
                    continue
                if mazeGraph[nx][ny] == 1:
                    mazeGraph[nx][ny] = mazeGraph[x][y]+1
                    queue.append((nx, ny))
        return mazeGraph[n-1][m-1]
    print(escape(0,0))

maze()