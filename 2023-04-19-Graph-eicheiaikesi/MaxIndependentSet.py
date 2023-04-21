from mip import Model, xsum, maximize, minimize, \
    BINARY, CONTINUOUS , MAXIMIZE, MINIMIZE, CBC
import networkx as nx

from collections import defaultdict

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
M = Model("Maximum Size Independent Set", sense=MAXIMIZE, solver_name=CBC)

x = [M.add_var(var_type=BINARY) for i in range(n)]

M.objective = maximize(xsum(x[i] for i in range(n)))

for e in G.edges:
    M += x[e[0]] + x[e[1]] <= 1
      
M.optimize()

selected = [V[i] for i in range(n) if x[i].x >= 0.99]
print("Nodes in maximum size independent set: {}".format(selected))

#---- Max matching ----
M = Model("Maximum Matching", sense=MAXIMIZE, solver_name=CBC)

x = [M.add_var(var_type=BINARY) for i in range(m)]

M.objective = maximize(xsum(x[i] for i in range(m)))

node_to_edges = defaultdict(list)
for (i, e) in enumerate(list(G.edges)):
    node_to_edges[e[0]].append(i)
    node_to_edges[e[1]].append(i)

for k, vs in node_to_edges.items():
    M += sum([x[v] for v in vs]) <= 1

M.optimize()

selected = [E[i] for i in range(m) if x[i].x >= 0.99]
print("Edges in maximum matching: {}".format(selected))

#---- minimum vertex covering ----
M = Model("Minimum vertex covering", sense=MINIMIZE, solver_name=CBC)

x = [M.add_var(var_type=BINARY) for i in range(n)]

M.objective = minimize(xsum(x[i] for i in range(n)))

for e in G.edges:
    M += x[e[0]] + x[e[1]] >= 1

M.optimize()

selected = [V[i] for i in range(n) if x[i].x >= 0.99]
print("Vertices in minimum vertex covering {}".format(selected))

#---- Fractional max matching ----
M = Model("Maximum Fractional Matching", sense=MAXIMIZE, solver_name=CBC)

x = [M.add_var(var_type=CONTINUOUS) for i in range(m)]

M.objective = maximize(xsum(x[i] for i in range(m)))

node_to_edges = defaultdict(list)
for (i, e) in enumerate(list(G.edges)):
    node_to_edges[e[0]].append(i)
    node_to_edges[e[1]].append(i)

for k, vs in node_to_edges.items():
    M += sum([x[v] for v in vs]) <= 1
    M += sum([x[v] for v in vs]) >= 0

M.optimize()

selected = [(E[i], x[i].x) for i in range(m)]
print("(Edges, Weight) in maximum fractional matching: {}".format(selected))