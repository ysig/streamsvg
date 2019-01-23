from streamsvg import Drawing

sg = Drawing()

sg.addNode("a")
sg.addNode("b")
sg.addNode("c")
sg.addNode("d")

sg.addLink("a", "b", 0, 7)
sg.addLink("b", "c", 1, 2)
sg.addLink("b", "c", 4, 8)
sg.addLink("b", "d", 9, 10)
sg.addLink("c", "d", 0, 5)

# Cluster A
sg.addNodeCluster("a", [(0,3)], color='pink', width=3)
sg.addNodeCluster("b", [(7,10)], color='pink', width=3)

# Cluster B
sg.addNodeCluster("b", [(2,6)], color='blue', width=3)
sg.addNodeCluster("d", [(8,10)], color='blue', width=3)

# Cluster C
sg.addNodeCluster("c", [(3,8)], color='green', width=3)
sg.addNodeCluster("d", [(0,5)], color='green', width=3)

sg.addTimeLine(ticks=2)

