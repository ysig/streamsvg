from streamsvg import Drawing

s = Drawing(alpha=0, omega=10)

s.addNode("u")
s.addNode("v")
s.addNode("x")

s.addRectangle("u", "v", 4, 6, color='green')

s.addLink("u", "v", 1.5, 6, curving=0.2)
s.addLink("v", "x", 3, 5)

s.addPath([(2, "u", "v"), (4, "v", "x")], 1, 9, width=2, color='blue')

s.addTimeLine(ticks=2)
