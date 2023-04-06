from mip import Model, xsum, maximize, minimize, BINARY
import networkx as nx

#---- Graph ----
G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,0)

n = G.number_of_nodes()
m = G.size()

V = list(G.nodes)
E = list(G.edges)

#---- Max Independent Set IP ----
M = Model("Maximum Size Independent Set")

x = [M.add_var(var_type=BINARY) for i in range(n)]

M.objective = maximize(xsum(x[i] for i in range(n)))

for e in G.edges:
    M += x[e[0]] + x[e[1]] <= 1
      
M.optimize()

selected = [V[i] for i in range(n) if x[i].x >= 0.99]
print("Nodes in maximum size independent set: {}".format(selected))
