# this is the property of edwin, the sexiest coder alive
# nahi samaj mein aa raha hai ye code toh chuulu bhar paani mein dub maro
# mereko dm mat karna doubts ke sath
# If the user is a member of the fairer sex call +91 89285 72970 for 1 on 1 sessions 5000 per session

class DFS:
	number_of_Edges = 0
	adjacencyMatrix = []
	def __init__(self,number_of_Edges,adjacencyMatrix):
		self.number_of_Edges= number_of_Edges
		self.adjacencyMatrix = adjacencyMatrix
		self.visited = [0]*number_of_Edges

	def traverse(self,source):
	    print(source)
	    # adding the node to the visited list
	    self.visited[source] = 1
	    for i in range(self.number_of_Edges):
	    	if self.adjacencyMatrix[source][i] == 1 and self.visited[i] == 0:
	    		self.traverse(i)
					
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

	dfs = DFS(n,adjacencyMatrix)
	dfs.traverse(4)

if __name__ == "__main__":
	main()