from streamsvg import Drawing

sg = Drawing()

sg.addNode("a", [(0,3), (7,10)])
sg.addNode("b")
sg.addNode("c", [(0,5)])

sg.addLink("a", "b", 0, 2)
sg.addLink("a", "b", 7, 10)
sg.addLink("b", "c", 2, 5)

# Cluster C
sg.addNodeCluster("b", [(1,3),(6,10)], color='blue')
sg.addNodeCluster("a", [(7,9)], color='blue')

# Neighborhood of C, N(C)
sg.addNodeCluster("a", [(1,2), (7,10)], width=5, color='brown')
sg.addNodeCluster("c", [(2,3)], width=5, color='brown')
sg.addNodeCluster("b", [(7,9)], width=5, color='brown')

sg.addTimeLine(ticks=2)

