def topo_sort(graph, nodes):

    # input: a directed acyclic graph (DAG)
    # returns: the post numbers of the nodes as an array of length num_nodes

    visited = set()
    post_numbers = {}
    cur_time = [0]

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        cur_time[0] += 1

        for neighbor in graph[node]:
            dfs(neighbor)
        
        post_numbers[node] = cur_time[0]
        cur_time[0] += 1

    for node in nodes:
        dfs(node)
    
    res = nodes[::]
    res.sort(key = lambda x: -post_numbers[x])
    return res


if __name__ == "__main__":
    from collections import defaultdict
    graph = defaultdict(set)
    before_graph = defaultdict(set)

    with open("input_1.txt", "r") as file:
        for line in file:
            number1, number2 = map(int, line.strip().split("|"))
            graph[number1].add(number2)
            before_graph[number2].add(number1)
    
    with open("input_2.txt", "r") as file:
        pages = []
        for line in file:
            numbers = list(map(int, line.strip().split(",")))
            pages.append(numbers)

    from collections import deque

    p1 = 0
    p2 = 0
    for page in pages:
        passes = True
        for i, num_1 in enumerate(page):
            for j, num_2 in enumerate(page):
                if i < j and num_2 in before_graph[num_1]:
                    passes = False
        
        if passes:
            p1 += page[len(page) // 2]
        
        else:
            # topo_sorted = topo_sort(graph, page)
            # p2 += topo_sorted[len(topo_sorted) // 2]
            
            good = []
            Q = deque([])
            D = {v: len(before_graph[v] & set(page)) for v in page}
            for v in page:
                if D[v] == 0:
                    Q.append(v)
            while Q:
                x = Q.popleft()
                good.append(x)
                for y in graph[x]:
                    if y in D:
                        D[y] -= 1
                        if D[y] == 0:
                            Q.append(y)
                
            p2 += good[len(good) // 2]

    print(p1)
    print(p2)