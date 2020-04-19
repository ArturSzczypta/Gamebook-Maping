import matplotlib.pyplot as plt

import matplotlib.animation as animation

import plotly.graph_objects as go

import networkx as nx

import numpy as np

import csv

#from intertools import combinations  as com

G = nx.Graph()
dicts = {}
distance = 20

with open('Gamebook Nodes.csv') as nodesFile:
	readCSVNodes= csv.reader(nodesFile, delimiter=',')

	
	for row in readCSVNodes:
		# Creating With and without special names
		if row[0] == row[1]:
			
			if int(row[0])%20 != 0:
				G.add_node(int(row[0]), name='', pos=(-int(row[0])%20,-(int(row[0])//20+1)))
			else:
				G.add_node(int(row[0]), name='', pos=(-(int(row[0])%20),-(int(row[0])//20)))

		else:
			
			if int(row[0])%20 != 0:
				G.add_node(int(row[0]), name=row[1], pos=(-int(row[0])%20,-(int(row[0])//20+1)))
			else:
				G.add_node(int(row[0]), name=row[1], pos=(-(int(row[0])%20),-(int(row[0])//20)))
		
		

#print('dictionary', dicts)


with open('Gamebook Edges.csv') as edgesFile:
	readCSVEdges= csv.reader(edgesFile, delimiter=',')

	for row in readCSVEdges:

		if row[1] != '':
			G.add_edge(int(row[0]), int(row[1]))

 #I have to create a dictionary wSBith values
 # https://networkx.github.io/documentation/latest/_downloads/networkx_reference.pdf page 680




#pos = nx.spring_layout(G, dim=40, k=None, fixed=None, iterations=10, weight='weight', scale=1.0, center=None)
#print(pos)
#print(G.nodes.data())
print('-----------')

position = nx.get_node_attributes(G, 'pos')

good_keys = [75,145,258]
bad_keys = [50,125,322]
failed = [139,182,198]
dead = [64,118,387]

#points = good_keys + [1,400]
#print(points)


#Shortest from point to point
#path = nx.shortest_path(G,source=1,target=400)



good_keys = [75,145,258]
bad_keys = [50,125,322]
failed = [139,182,198]
dead = [64,118,387]
print(path)

pos = nx.spring_layout(G, pos=position, fixed=[1,400], iterations=0)

nx.draw(G, pos, dim=1, node_color='green', node_size=50, with_labels=True,\
    width= 1,alpha=1, font_size=8,font_weight='normal')
#print(nx.spring_layout(G, pos=position, fixed=[1, 400], iterations=10))
#print(pos)
#nx.draw_networkx_edges(G,pos,arrows=True,arrowstyle='-|>', arrowsize=10)




#path_edges = zip(path,path[1:])

# get solution to be a line. Make it so itsteadly becoming straight line
# those 9 connected points from the begining to the end should be bolded
# stop those few points from flying away
# point out deaths and wrong keys


nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='blue', node_size=80)
nx.draw_networkx_nodes(G,pos,nodelist=good_keys,node_color='cyan', node_size=80)
nx.draw_networkx_nodes(G,pos,nodelist=bad_keys,node_color='purple', node_size=80)
nx.draw_networkx_nodes(G,pos,nodelist=bad_keys,node_color='orange', node_size=80)
nx.draw_networkx_nodes(G,pos,nodelist=dead,node_color='red', node_size=80)
print(path)
#nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)



plt.axis('equal')




special_ones = nx.get_node_attributes(G, 'after_iterating')
plt.show()
print('---------------')
print(special_ones)
plt.savefig("graph.png")
#nx.draw_networkx_nodes(G,pos=after_iterating,nodelist=[0,400], node_color='b')

'''
 Animation based on answer from @david
https://stackoverflow.com/questions/61261107/smooth-animation-of-a-network-using-networkx-and-matplotlib

node_number = 0
while node_number < 10:
    pos = nx.spring_layout(G, pos=position, fixed=[1,400], iterations=node_number)
    node_number += 1


def anim(t):
    global s_pos
    global t_pos
    interpolation = {i: s_pos[i]*(1-t/10) + t_pos[i] * t/10  for i in range(10)}
    plt.clf()
    plt.cla()
    nx.draw(G, pos=interpolation)


ani = animation.FuncAnimation(G, anim, repeat=False, frames=10, interval=10)
plt.show()


iteration = 0
def simple_update(num, n, layout, G, ax):
    ax.clear()

    pos = nx.spring_layout(G, pos=position, fixed=[1,400], iterations=iteration)
    nx.draw(G, pos, dim=1, node_color='green', node_size=50, with_labels=True,\
    width= 1,alpha=1, font_size=8,font_weight='normal')

    ax.set_title("Frame {}".format(num))

    iteration += 1



# Build plot
fig, ax = plt.subplots(figsize=(10,10))

# Create a graph and layout
n = 30 # Number of nodes
m = 70 # Number of edges
G = nx.gnm_random_graph(n, m)
layout = nx.spring_layout(G)

ani = animation.FuncAnimation(fig, simple_update, frames=10, fargs=(n, layout, G, ax))


plt.show()




























edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.node[edge[0]][pos[0]]
    x1, y1 = G.node[edge[1]][pos[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.node[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

# Color Node Points
node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append(str(node + 1) + ' connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

# Create Network Graph
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()

'''