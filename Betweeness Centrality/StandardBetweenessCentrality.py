#!/usr/bin/env python3
import copy
import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
	name = "Sanchit Trivedi"
	email = "dummy@iiitd.ac.in"
	roll_num = "2010000"

	def __init__ (self, vertices, edges):
		"""
		Initializes object for the class Graph
		Args:
			vertices: List of integers specifying vertices in graph
			edges: List of 2-tuples specifying edges in graph
		"""
		self.vertices = vertices
		ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
		self.edges    = ordered_edges
		self.validate()
		self.graphcreator()
		self.minpath_dict={}
		self.all_shortest_paths_dict={}
		self.countwithoutnode={}
		self.countwithnode={}
		self.betweennesscentrality={}
		self.stdbetweennesscentrality={}
		l=self.vertices
		self.pairs=[]
		for i in range(len(l)):
			for j in range (i+1,len(l)):
				self.pairs.append((l[i],l[j]))
		#print(self.pairs)
		self.top_k_betweenness_centrality()
		#print(self.minpath_dict)
		#print (self.all_shortest_paths_dict)
		
	def validate(self):
		"""
		Validates if Graph if valid or not
		Raises:
			Exception if:
				- Name is empty or not a string
				- Email is empty or not a string
				- Roll Number is not in correct format
				- vertices contains duplicates
				- edges contain duplicates
				- any endpoint of an edge is not in vertices
		"""
		if (not isinstance(self.name, str)) or self.name == "":
			raise Exception("Name can't be empty")

		if (not isinstance(self.email, str)) or self.email == "":
			raise Exception("Email can't be empty")

		if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
			raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

		if not all([isinstance(node, int) for node in self.vertices]):
			raise Exception("All vertices should be integers")

		elif len(self.vertices) != len(set(self.vertices)):
			duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])
			raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

		edge_vertices = list(set(itertools.chain(*self.edges)))

		if not all([node in self.vertices for node in edge_vertices]):
			raise Exception("All endpoints of edges must belong in vertices")

		if len(self.edges) != len(set(self.edges)):
			duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])
			raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))
	
	def graphcreator(self):
		self.graph_dict={}
		n=len(self.edges)
		for i in range(n):
			t=(self.edges[i][1],self.edges[i][0])
			self.edges.append(t)
		for i in self.vertices:
			l=[]
			for j in self.edges:
				if j[0]==i:
					l.append(j[1])
			self.graph_dict[i]=l
		#print ('graph_dict= ',self.graph_dict)	

	def min_dist(self, start_node, end_node):
		'''
		Finds minimum distance between start_node and end_node
		Args:
			start_node: Vertex to find distance from
			end_node: Vertex to find distance to
		Returns:
			An integer denoting minimum distance between start_node
			and end_node
		'''
		q = [str(start_node)]
		visited = []
		g=self.graph_dict
		while len(q):
			path = q.pop(0)
			node = path[-1]
			if node in visited:
				pass
			else:
				neighbours = g[int(node)]
				for i in neighbours:
					new_path = str(path)
					if str(i) not in new_path:
						new_path+='--'
						new_path+=str(i)
					q.append(new_path)
					if i==end_node:
						return new_path
				visited.append(node)

	def all_shortest_paths(self,start_node, end_node):
		"""
		Finds all shortest paths between start_node and end_node
		Args:
			start_node: Starting node for paths
			end_node: Destination node for paths
		Returns:
			A list of path, where each path is a list of integers.
		"""
		i=(start_node,end_node)
		self.minpath_dict[i]=self.min_dist(start_node,end_node)
		self.all_shortest_paths_dict[i]=self.all_paths(start_node,end_node,(self.minpath_dict[i].count('--')))

	def all_paths(self,node,destination,dist,path=[]):
		"""
		Finds all paths from node to destination with length = dist
		Args:
			node: Node to find path from
			destination: Node to reach
			dist: Allowed distance of path
			path: path already traversed
		Returns:
			List of path, where each path is list ending on destination
			Returns None if there no paths
		"""
		graph = self.graph_dict 
		path = path + [node]
		if node == destination:
			return [path]
		paths = []
		
		for vertex in graph[node]:
			if vertex in path:
				pass
			else:
				extended_paths = self.all_paths(vertex,destination,dist,path)
				for p in extended_paths: 
						paths.append(p)
		final_paths=[]
		for i in paths:
			if (len(i)-1)==dist:
				final_paths.append(i)
		return final_paths
	
	def betweenness_centrality(self, node):
		"""
		Find betweenness centrality of the given node
		Args:
			node: Node to find betweenness centrality of.
		Returns:
			Single floating point number, denoting betweenness centrality
			of the given node
		"""
		n=len(self.vertices)
		ydivix={}
		self.countwithnode.clear();self.countwithoutnode.clear()
		pairstocheck=copy.deepcopy(self.pairs)
		#print(pairstocheck)
		for i in self.pairs:
			if node in i:
				pairstocheck.remove(i)
		#print(pairstocheck)
		for j in pairstocheck:
			x,y=j
			self.all_shortest_paths(x,y)
		for j in pairstocheck:
			self.countwithnode[j]=len(self.all_shortest_paths_dict[j])
			self.countwithoutnode[j]=len(self.all_shortest_paths_dict[j])
			for i in self.all_shortest_paths_dict[j]:
				if node not in i:
					self.countwithoutnode[j]-=1
		#print(self.countwithnode);print(self.countwithoutnode)
		for j in pairstocheck:
			ydivix[j]=(self.countwithoutnode[j]/self.countwithnode[j])
		self.betweennesscentrality[node]=sum(ydivix.values())
		self.stdbetweennesscentrality[node]=((2*self.betweennesscentrality[node])/((n-1)*(n-2)))

	def top_k_betweenness_centrality(self):
		"""
		Find top k nodes based on highest equal betweenness centrality.
		Returns:
			List a integer, denoting top k nodes based on betweenness
			centrality.
		"""
		for i in self.vertices:
			self.betweenness_centrality(i)
		print(self.betweennesscentrality)
		print (self.stdbetweennesscentrality)
		k=max(self.stdbetweennesscentrality.values())
		topknodes=[]
		for j in self.stdbetweennesscentrality:
			if self.stdbetweennesscentrality[j]==k:
				topknodes.append(j)
		print (topknodes) 


if __name__ == "__main__":
	vertices = [1, 2, 3, 4, 5, 6]
	edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6)]
	graph = Graph(vertices, edges)