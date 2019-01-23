from streamsvg import Drawing

s = Drawing(alpha=0, omega=10)

s.addNode("a", color='green')
s.addNode("u", color='red')
s.addNode("b", color='green')
s.addNode("v", color='red')
s.addNode("c", color='green')

s.addLink("a", "u", 0, 2)
s.addLink("a", "u", 3, 9)
s.addLink("b", "u", 4, 5)
s.addLink("b", "u", 8, 10)
s.addLink("b", "v", 2, 7)
s.addLink("c", "u", 1, 5, height=0.55)
s.addLink("c", "v", 0, 8)

s.addTimeLine(ticks=2)
