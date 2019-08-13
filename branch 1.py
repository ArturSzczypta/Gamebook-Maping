import plotly.graph_objects as go

import networkx as nx

import csv

G = nx.Graph()

with open('Gamebook Nodes.csv') as nodesFile:
	readCSVNodes= csv.reader(nodesFile, delimiter=',')

	for row in readCSVNodes:
		if row[0] == row[1]:
			
			if int(row[0])%20 != 0:
				G.add_node(int(row[0]), name='', pos=(int(row[0])%20,int(row[0])//20))
			else:
				G.add_node(int(row[0]), name='', pos=(int(row[0])%20 + 20,int(row[0])//20 - 1))

		else:
			
			if int(row[0])%20 != 0:
				G.add_node(int(row[0]), name=row[1], pos=(int(row[0])%20,int(row[0])//20))
			else:
				G.add_node(int(row[0]), name=row[1], pos=(int(row[0])%20  + 20,int(row[0])//20 - 1))


with open('Gamebook Edges.csv') as edgesFile:
	readCSVEdges= csv.reader(edgesFile, delimiter=',')

	for row in readCSVEdges:

		if row[1] != '':
			G.add_edge(int(row[0]), int(row[1]))

 #I have to create a dictionary with values
 # https://networkx.github.io/documentation/latest/_downloads/networkx_reference.pdf page 680




#nx.spring_layout(G, dim=40, k=None, pos=dict, fixed=None, iterations=50, weight='weight', scale=1.0, center=None)

print(G.nodes.data())
print(G.edges)










		
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.node[edge[0]]['pos']
    x1, y1 = G.node[edge[1]]['pos']
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
    node_text.append(str(node + 1) + node('name')+ ' connections: '+str(len(adjacencies[1])))

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

