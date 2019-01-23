from streamsvg import Drawing

s = Drawing(alpha=0, omega=10)

s.addNode("u")
s.addNode("v")
s.addNode("w")

s.addLink("u", "v", 1, 2)
s.addLink("v", "w", 3, 4)
s.addLink("u", "v", 5, 6)
s.addLink("v", "w", 8, 9)

s.addPath(((2,"u","v"), (3, "v", "w")), 2, 3, color="#AEC7E8", width=2)
s.addPath(((6,"u","v"), (8, "v", "w")), 6, 8, color="#98DF8A", width=2)
s.addPath(((4,"w","v"), (5, "v", "u")), 4, 5, color="#FF9896", width=2)

s.addTimeLine(ticks=2)
