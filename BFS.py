from queue import Queue

class BFS:
	number_of_Edges = 0
	adjacencyMatrix = []
	def __init__(self,number_of_Edges,adjacencyMatrix):
		self.number_of_Edges= number_of_Edges
		self.adjacencyMatrix = adjacencyMatrix
		self.visited = []*number_of_Edges

	def traverse(self,source):
	    q = Queue(maxsize=50)
	    visited = [0]*self.number_of_Edges
	    print("Node:"+str(source))
	    visited[source] = 1
	    q.put(source)
	    while not q.empty():
	        node = q.get()
	        for j in range(self.number_of_Edges):
	            if self.adjacencyMatrix[node][j] == 1 and visited[j] == 0:
	                print("Node:"+str(j))
	                visited[j] = 1
	                q.put(j)
					
def main():
	n=7
	adjacencyMatrix = [
		[0,1,1,1,0,0,0],
		[1,0,1,0,0,0,0],
		[1,1,0,1,1,0,0],
		[1,0,1,0,1,0,0],
		[0,0,1,1,0,1,1],
		[0,0,0,0,1,0,0],
		[0,0,0,0,1,0,0]
	]

	bfs = BFS(n,adjacencyMatrix)
	bfs.traverse(1)

if __name__ == "__main__":
	main()