from collections import deque

graph = {
    "S": ["A", "B", "C"],
    "A": ["D", "E"],
    "B": ["G"],
    "C": ["F"],
    "D": ["H"],
    "E": ["G"],
    "F": ["G"],
    "G": [],
    "H": []
}


def bfs(graph, start, goal):
    frontier = deque([(start, [start])])

    testedNodes = 0
    expandedNodes = 0

    print("Expand Node\tFrontier List")
    print(f"-\t\t[{start}]")

    while frontier:
        currentNode, currentPath = frontier.popleft()
        testedNodes += 1

        if currentNode == goal:
            frontierNodes = [item[0] for item in frontier]
            print(f"{currentNode}\t\t{frontierNodes}")

            print("\nGoal node found!")
            print("Path:", " -> ".join(currentPath))
            print(f"Nodes tested: {testedNodes}")
            print(f"Nodes expanded: {expandedNodes}")
            return currentPath

        for neighbor in graph[currentNode]:
            newPath = currentPath + [neighbor]
            frontier.append((neighbor, newPath))

        expandedNodes += 1

        frontierNodes = [item[0] for item in frontier]
        print(f"{currentNode}\t\t{frontierNodes}")

    print("\nGoal node was not found.")


search = bfs(graph, "S", "G")
