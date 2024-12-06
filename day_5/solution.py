graph = {1: [1, 2, 3]}

def topo_sort(graph):

    # input: a directed acyclic graph (DAG)
    # returns: the post numbers of the nodes as an array of length num_nodes

    visited = set()
    post_numbers = [-1 for _ in range(len(graph))]
    cur_time = 0

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        cur_time += 1

        for neighbor in graph[node]:
            dfs(neighbor)
        
        post_numbers[node] = cur_time
        cur_time += 1

    for node, neighbors in graph.items():
        dfs(node)
    
    return post_numbers


if __name__ == "__main__":
    from collections import defaultdict
    graph = defaultdict(list)

    with open("input_1.txt", "r") as file:
        for line in file:
            number1, number2 = map(int, line.strip().split("|"))
            graph[number1].append(number2)
    
    post_numbers = topo_sort(graph)
    print(post_numbers)