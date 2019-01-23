from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b")
s.addNode("c")
s.addNode("d")

s.addLink("a", "b", 0, 4,color="#BBBBBB",width=2)
s.addLink("a", "b", 6, 9,color="#BBBBBB",width=2)
s.addLink("a", "c", 2, 5, height=0.4,width=3)
s.addLink("b", "c", 1, 8,width=3)
s.addLink("b", "d", 7, 10, height=0.4,color="#BBBBBB",width=2)
s.addLink("c", "d", 6, 9,width=3)

s.addNodeCluster("a",[(2,5)],color="blue",width=3)
s.addNodeCluster("b",[(1,8)],color="blue",width=3)
s.addNodeCluster("d",[(6,9)],color="blue",width=3)

s.addTimeLine(ticks=2)

