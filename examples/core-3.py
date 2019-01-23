from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b")
s.addNode("c")
s.addNode("d")

s.addNodeCluster("a",[(0,1),(6,10)], color="#AEC7E8", width=5)
s.addNodeCluster("b",[(0,3)], color="#AEC7E8", width=5)
s.addNodeCluster("c",[(0,1),(9,10)], color="#AEC7E8", width=5)
s.addNodeCluster("d",[(0,2)], color="#AEC7E8", width=5)

s.addNodeCluster("a",[(1,4),(5,6)], color="#98DF8A", width=5)
s.addNodeCluster("b",[(3,4),(5,7),(9,10)], color="#98DF8A", width=5)
s.addNodeCluster("c",[(1,4),(5,7)], color="#98DF8A", width=5)
s.addNodeCluster("d",[(2,4),(5,7),(9,10)], color="#98DF8A", width=5)

s.addNodeCluster("a",[(4,5)], color="#FF9896", width=5)
s.addNodeCluster("b",[(4,5),(7,9)], color="#FF9896", width=5)
s.addNodeCluster("c",[(4,5),(7,9)], color="#FF9896", width=5)
s.addNodeCluster("d",[(4,5),(7,9)], color="#FF9896", width=5)

s.addTimeLine(ticks=2)

