import networkx as nx

G = nx.read_weighted_edgelist("NAFLD.txt",comments="#",nodetype=str)

T = ['YDL219W', 'YML087C', 'YMR212C', 'YLL061W', 'YCR026C', 'YCR028C-A', 'YLR001C', 'YLL055W', 'YDR236C', 'YBR046C', 'YCR028C', 'YML125C', 'YBL057C', 'YAL067C', 'YKR013W', 'YOL119C', 'YER159C', 'YBR233W', 'YDR105C', 'YGR065C', 'YPR131C', 'YHR078W', 'YDR371W', 'YLR004C', 'YJL079C', 'YDR221W', 'YJR001W', 'YCR075C', 'YOR093C', 'YER140W', 'YPR058W', 'YJR085C', 'YOR280C', 'YOR256C', 'YBR210W', 'YBR104W', 'YLL048C', 'YPL088W', 'YJR100C', 'YKL198C', 'YDR151C', 'YDR338C', 'YGL159W', 'YJR126C', 'YGL096W', 'YDR372C']

# Parameters
name = "Yeast PPIN with non-isolated nodes associated with NAFLD removed"
creator = "A. Habibi"

f = open("NAFLD_graph.stp", "w")

# Header
f.write("33D32945 STP File, STP Format Version 1.0\n\n")

# Comments
f.write("SECTION Comment\n")
f.write(f"Name\t\"{name}\"\n")
f.write(f"Creator\t\"{creator}\"\n")
f.write("END\n\n")

# Graph
f.write("SECTION Graph\n")
n = G.number_of_nodes()
m = G.number_of_edges()
f.write(f"Nodes {n}\n")
f.write(f"Edges {m}\n")

# STP requires nodes to be represented by positive integers. So, we use index + 1 of nodes in node list of G.
node_key = {}
for index, node in enumerate(G.nodes()):
  node_key[node] = index + 1

for (u, v, d) in G.edges().data():
  f.write(f"E {node_key[u]} {node_key[v]} {int(d['weight'])}\n")
f.write("END\n\n")

# Terminals
f.write("SECTION Terminals\n")
f.write(f"Terminals {len(T)}\n")
for t in T:
  f.write(f"T {node_key[t]}\n")
f.write("END\n\n")

f.write("EOF")

f.close()