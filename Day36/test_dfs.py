def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # We need an adjacency list because;
    # we need to find all courses dependent of others
    # we need to explore all the neighbors of a node
    # we need to use dfs or bfs on the graph
    graph = [[] for _ in range(numCourses)]

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0=Unvisited, 1=visiting, 2=visited, completed
    colors = [0] * numCourses # marking all nodes as unvisited
    def dfs(course):
        if colors[course] == 1:
            return True
        if colors[course] == 2:
            return False

        colors[course] = 1 # indicate we're still visiting the course

        for next_c in graph:
            if dfs(next_c):
                return True
        colors[course] = 2
        return False

    for course in range(numCourses):
        if dfs(course):
            return True
    return False

print(canFinish(1, [[1,0], [0,3], [3, 2], [2, 1]]))