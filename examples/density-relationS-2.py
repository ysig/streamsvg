from streamsvg import Drawing

sg = Drawing(alpha=0, omega=3)
sg.addNode("a", [(0,1)])
sg.addNode("b")
sg.addNode("c", [(1,3)])

sg.addLink("a", "b", 0, 1)
sg.addLink("b", "c", 1, 3)

sg.addTimeLine(ticks=1)

