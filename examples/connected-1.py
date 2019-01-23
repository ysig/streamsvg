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

s.addNodeCluster("a", [(0,5)], color='blue',width=5)
s.addNodeCluster("b", [(0,5)], color='blue',width=5)
s.addNodeCluster("c", [(0,5)], color='blue',width=5)
s.addNodeCluster("a", [(5,10)], color='blue',width=7)
s.addNodeCluster("b", [(5,10)], color='blue',width=7)
s.addNodeCluster("c", [(5,10)], color='blue',width=7)
s.addNodeCluster("d", [(5,10)], color='blue',width=7)
s.addNodeCluster("e", [(5,10)], color='blue',width=7)

s.addNodeCluster("a", [(5,10)], color="#FF9896",width=5)
s.addNodeCluster("b", [(5,10)], color="#FF9896",width=5)
s.addNodeCluster("c", [(5,10)], color="#FF9896",width=5)
s.addNodeCluster("d", [(0,10)], color="#FF9896",width=5)
s.addNodeCluster("e", [(0,10)], color="#FF9896",width=5)


s.addTimeLine(ticks=2)
