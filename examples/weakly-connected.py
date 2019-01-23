from streamsvg import Drawing

s = Drawing()

s.addNode("a", [(5,7)])
s.addNode("b", [(0,3), (5,7), (8,10)])
s.addNode("c", [(0,10)])
s.addNode("d", [(0,2), (3,7), (8,10)])
s.addNode("e", [(0,10)])
s.addNode("f", [(0,4), (7,10)])
s.addNode("g", [(0,4), (5,10)])

# wcc 1
s.addNodeCluster("a",[(5,7)], color="#AEC7E8", width=3)
s.addNodeCluster("b",[(5,7)], color="#AEC7E8", width=3)
# wcc 2
s.addNodeCluster("b",[(0,3), (8,10)], color="#FF9896", width=3)
s.addNodeCluster("c",[(0,10)], color="#FF9896", width=3)
s.addNodeCluster("d",[(3,7)], color="#FF9896", width=3)
# wcc 3
s.addNodeCluster("d",[(0,2), (8,10)], color="#98DF8A", width=3)
s.addNodeCluster("e",[(0,10)], color="#98DF8A", width=3)
s.addNodeCluster("f",[(0,4)], color="#98DF8A", width=3)
s.addNodeCluster("g",[(0,4)], color="#98DF8A", width=3)
# wcc 4
s.addNodeCluster("f",[(7,10)], color="#FFBB78", width=3)
s.addNodeCluster("g",[(5,10)], color="#FFBB78", width=3)


s.addLink("a", "b", 5.5, 6.5)
s.addLink("b", "c", 1, 3)
s.addLink("b", "c", 9, 10)
s.addLink("c", "d", 4, 6)
s.addLink("d", "e", 0.5, 1.5)
s.addLink("d", "e", 8, 10)
s.addLink("e", "f", 2, 4)
s.addLink("f", "g", 0, 2)
s.addLink("f", "g", 8.5, 9.5)

s.addTimeLine(ticks=2)
