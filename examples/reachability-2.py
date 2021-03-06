from streamsvg import Drawing

sg = Drawing()

sg.addNode("u")
sg.addNode("v")
sg.addNode("w")

sg.addLink("u", "v", 1,3)
sg.addLink("v", "w", 4,6)
sg.addLink("u", "v", 7,9)

sg.addNodeCluster("u", [(0,3)], color='green')
sg.addNodeCluster("v", [(0,6)], color='pink')
sg.addNodeCluster("w", [(0,6)], color='blue')

sg.addTimeLine(ticks=2)
