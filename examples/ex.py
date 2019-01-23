from streamsvg import Drawing

s = Drawing(alpha=0, omega=10, discrete=1.5)

s.addNode("u")
s.addNode("v")
s.addNode("x")
s.addNode("y", [(3,6)])

s.addNodeCluster("u", [(0.5,2)], color='blue', width=200)
s.addNodeCluster("v", color='blue')
s.addNodeCluster("u", [(6,7.5)], color="#ff0000")

s.addLink("u", "v", 1.5, 6)
s.addLink("u", "x", 1.5, 1.5, curving=0.2)
s.addLink("v", "y", 1.5, 1.5, curving=-0.2)
