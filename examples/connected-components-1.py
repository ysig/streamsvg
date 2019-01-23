from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b")
s.addNode("c")
s.addNode("d")
s.addNode("e")

s.addLink("a", "b", 0, 10)
s.addLink("b", "c", 0, 3)
s.addLink("a", "c", 2, 10, height=0.4)
s.addLink("c", "d", 5, 10)
s.addLink("d", "e", 0, 10)

s.addRectangle("a", "c", -0.1, 4.95, color="none", bordercolor="#AEC7E8")
s.addRectangle("d", "e", -0.1, 4.95, color="none", bordercolor="#AEC7E8")
s.addRectangle("a", "e", 5, 10.1, color="none", bordercolor="#AEC7E8")

s.addTimeLine(ticks=2)

