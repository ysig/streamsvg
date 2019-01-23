from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b")
s.addNode("c")
s.addNode("d")

s.addLink("a", "b", 0, 4, color='green')
s.addLink("a", "b", 6, 8, color='green')
s.addLink("b", "c", 2, 4, color='blue')
s.addLink("b", "c", 5, 7, color='orange')
s.addLink("b", "c", 9, 10, color='orange')
s.addLink("b", "d", 3, 5, color='orange', height=0.6)
s.addLink("c", "d", 7, 10, color='magenta')

s.addTimeLine(ticks=2)
