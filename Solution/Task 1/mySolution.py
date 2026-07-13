from collections import deque

def solution(N, A, B):
    graph = [[] for i in range(N)]
    degree = [0] * N
    removed = [False] * N
    queue = deque()
    ans = 0
    
    for i in range(len(A)):
        u = A[i]
        v = B[i]
        
        graph[u].append(v)
        graph[v].append(u)
        
        degree[u] += 1
        degree[v] += 1
    
    for i in range(N):
        if degree[i] <= 1:
            queue.append(i)
            removed[i] = True
    
    while queue:
        size = len(queue)
        
        for _ in range(size):
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if removed[neighbor]:
                    continue
                
                degree[neighbor] -= 1
                if degree[neighbor] <= 1:
                    removed[neighbor] == True
                    queue.append(neighbor)
                    
        ans += 1
    return ans


# 測資
N = 7
A = [0, 1, 2, 1, 4, 4]
B = [1, 2, 0, 4, 5, 6]

print(solution(N, A, B))
