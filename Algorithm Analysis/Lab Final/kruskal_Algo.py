def find(parent, x):
    if parent[x] == -1:
        return x
    return find(parent, parent[x])

def union(parent, a, b):
    parent[find(parent, a)] = find(parent, b)


# Input
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
print("Enter edges (U V Weight):")

for _ in range(edges_count):
    data = input().split()     
    u = int(data[0])
    v = int(data[1])
    weight = int(data[2])
    edges.append((weight, u, v))

edges.sort()

parent = [-1] * vertices
mst_weight = 0
edge_count = 0

print("\nEdges in MST:")

for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        print(u, "-", v, ":", weight)
        mst_weight += weight
        union(parent, u, v)
        edge_count += 1
        if edge_count == vertices - 1:
            break

print("Total weight:", mst_weight)