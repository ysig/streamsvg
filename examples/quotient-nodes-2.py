from streamsvg import Drawing

sg = Drawing()

sg.addNode("A", [(0,3),(7,10)], color='pink')
sg.addNode("B", [(2,6),(8,10)], color='blue')
sg.addNode("C", [(0,8)], color='green')

sg.addLink("A", "B", 2, 3)
sg.addLink("A", "B", 9, 10)
sg.addLink("A", "C", 7, 8, height=0.6)
sg.addLink("B", "C", 4, 6)

sg.addTimeLine(ticks=2)

