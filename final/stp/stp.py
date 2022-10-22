import networkx as nx

# Returns node-integer mapping used
def nxgraph_to_stp(graph, terminals, filename):

  # Parameters
  name = "Yeast PPIN with non-isolated nodes associated with NAFLD removed"
  creator = "A. Habibi"

  f = open(filename, "w")

  # Header
  f.write("33D32945 STP File, STP Format Version 1.0\n\n")

  # Comments
  f.write("SECTION Comment\n")
  f.write(f"Name\t\"{name}\"\n")
  f.write(f"Creator\t\"{creator}\"\n")
  f.write("END\n\n")

  # Graph
  f.write("SECTION Graph\n")
  n = graph.number_of_nodes()
  m = graph.number_of_edges()
  f.write(f"Nodes {n}\n")
  f.write(f"Edges {m}\n")

  # STP requires nodes to be represented by positive integers. So, we use index + 1 of nodes in node list of G.
  node_key = {}
  for index, node in enumerate(graph.nodes()):
    node_key[node] = index + 1

  for (u, v, d) in graph.edges().data():
    f.write(f"E {node_key[u]} {node_key[v]} {int(d['weight'])}\n")
  f.write("END\n\n")

  # Terminals
  f.write("SECTION Terminals\n")
  f.write(f"Terminals {len(terminals)}\n")
  for t in terminals:
    f.write(f"T {node_key[t]}\n")
  f.write("END\n\n")

  f.write("EOF")

  f.close()

  return node_key


# Takes in an stplog file, an integer-node mapping (inverse of node_key above) and returns an nx graph.
def stplog_to_nxgraph(filename, int_to_node):
  G = nx.Graph()

  f = open(filename, "r")

  l = f.readlines()

  # Moving to final solution section
  i = l.index("SECTION Finalsolution\n")

  # Finding number of vertices
  n = int(l[i + 1].split(" ")[1])

  # Moving pointer down to start of vertices
  i += 2

  for j in range(0, n):
    node = int(l[i + j].split(" ")[1])
    G.add_node(int_to_node[node])

  # Since this is a tree, there will be n - 1 edges.
  i += n + 1

  for j in range(0, n-1):
    u, v = int(l[i + j].split(" ")[1]), int(l[i + j].split(" ")[2])
    G.add_edge(int_to_node[u], int_to_node[v], weight = 1)

  f.close()

  return G