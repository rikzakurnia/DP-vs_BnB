# Python3 implementation for the above approach
import sys
import timeit

# Set a higher recursion depth limit (e.g., 3000)
sys.setrecursionlimit(3000)

def addEdge(adj, x, y):
	adj[x].append(y)
	adj[y].append(x)


def dfs(adj, dp, src, par):
	for child in adj[src]:
		if child != par:
			dfs(adj, dp, child, src)

	for child in adj[src]:
		if child != par:
			# not including source in the vertex cover
			dp[src][0] = dp[child][1] + dp[src][0]

			# including source in the vertex cover
			dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])


def minSizeVertexCover(adj, N):
	dp = [[0 for j in range(2)] for i in range(N+1)]
	for i in range(1, N+1):
		# 0 denotes not included in vertex cover
		dp[i][0] = 0

		# 1 denotes included in vertex cover
		dp[i][1] = 1
	start_time = timeit.default_timer()
	dfs(adj, dp, 1, -1)
	end_time = timeit.default_timer()

	# printing minimum size vertex cover
	print(min(dp[1][0], dp[1][1]))
	time_taken = end_time - start_time
	print("Time taken by minSizeVertexCover: {:.5f} seconds".format(time_taken))


def readGraphFromFile(file_path, adj_list):
    
    with open(file_path, 'r') as file:
        num_nodes, num_edges, _ = map(int, file.readline().split())
        for _ in range(num_nodes):
            adj_list.append(list(map(int, file.readline().split())))
    return adj_list

# Example usage
file_path = 'medium.graph'  # Replace with the path to your .graph file
adj_list = []
adj_list.append([])
adj_list_from_file = readGraphFromFile(file_path, adj_list)
N = len(adj_list_from_file)

minSizeVertexCover(adj_list_from_file, N)



