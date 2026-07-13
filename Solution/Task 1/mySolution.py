def solution(N, A, B):
    graph = [[] for i in range(N)]
    degree = [0] * N
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
    
    while queue:
        size = len(queue)
        
        for _ in range(size):
            node = queue.popleft()
            
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)
        ans += 1
    return ans
