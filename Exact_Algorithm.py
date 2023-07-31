import networkx as nx
from itertools import chain, combinations
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import simpy
import time
from itertools import combinations

start_time = time.time()

G = nx.cycle_graph(17)

def calculate_combinations(lst, r):
    combinations_list = list(combinations(lst, r))
    return combinations_list

def neighbors(G):
    ng = {}
    for i in G.nodes():
        modng = list(G[i]) + [i]
        ng[i] = modng
    return ng

neighbors(G)
nbrs = neighbors(G)


def neighborsset(v):
    a = []
    for i in v:
        a += nbrs[i]
    return set(a)


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def subsets(G):
    i = []
    for node in powerset(G.nodes):
        i.append(tuple(node))
    return i


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


cg = nx.Graph()


def configurationGraph(v):
    cg.add_nodes_from(v)

    edges_to_add = []

    for i in cg.nodes:
        lis = list()
        if i != ():
            for j in i:
                lis += nbrs[j]
        lis = list(set(lis))
        rem_ver = list()
        rem_ver = Diff(list(G.nodes), list(i))
        for j in rem_ver:
            lis1 = lis + [j]
            edges_to_add.append((i, tuple(set(lis1))))

    cg.add_edges_from(edges_to_add)  # Add edges outside the loop
    print("Burning Sequence :",nx.shortest_path(cg,source=(),target=v[-1]))
    burning_sequence=nx.shortest_path(cg,source=(),target=v[-1])
    print("Burning Number :",len(nx.shortest_path(cg,source=(),target=v[-1]))-1)
    burning_number = len(nx.shortest_path(cg,source=(),target=v[-1]))-1
    return(burning_sequence,burning_number)

burning_sequence,burning_number=configurationGraph(subsets(G))
end_time = time.time()
print("Running time :",end_time-start_time)

def burnNode(env,nodes):
  count=0
  while True:
    print("Started burning node(s)",nodes[count],"at %d" % env.now)
    duration = 2
    yield env.timeout(duration)
    count+=1

def simulate(burning_sequence):
  env=simpy.Environment()
  env.process(burnNode(env,burning_sequence))
  env.run(until=burning_number*2)

simulate(burning_sequence[1:])

def visualize(burning_sequence,burning_number):
  fig, ax = plt.subplots()
  def animate(i):
        ax.clear()
        current_set=burning_sequence[min(i,burning_number)]
        burnt=list(current_set)
        node_colors = ['red' if node in burnt else 'blue' for node in G.nodes()]
        pos = nx.spring_layout(G, seed=50)
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=10)
        ax.set_title(f"Graph Burning Animation")

  anim = animation.FuncAnimation(fig, animate, frames=burning_number+6, interval=1000, blit=False)
  anim.save("graphBurning.mp4", writer='ffmpeg', fps=1)

visualize(burning_sequence,burning_number)