from streamsvg import Drawing

s = Drawing(alpha=0, omega=10)

s.addNode("a", color='green')
s.addNode("u", color="none", rectangle_color="none")
s.addNode("b", color='green')
s.addNode("v", color="none", rectangle_color="none")
s.addNode("c", color='green')

s.addLink("a", "c", 1, 2, height=0.33)
s.addLink("a", "c", 3, 5, height=0.33)
s.addLink("a", "b", 4, 5)
s.addLink("a", "b", 8, 9)
s.addLink("b", "c", 2, 7)

s.addTimeLine(ticks=2)
