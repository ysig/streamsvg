from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b", [(0,4), (5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

s.addLink("a", "b", 1, 1, color='blue', width=3)
s.addLink("b", "d", 2, 2, color='blue', width=3)
s.addLink("a", "c", 4.5, 4.5, color='blue', width=3)
s.addLink("b", "c", 6, 6, color='blue', width=3)

s.addLink("a", "b", 1, 3)
s.addLink("b", "d", 2, 3)
s.addLink("a", "c", 4.5, 7.5, height=0.40)
s.addLink("a", "b", 7, 8)
s.addLink("b", "c", 6, 9)

s.addTimeNodeMark(0,"b",color="#FF9896",width=2)

s.addNodeCluster("a", [(1,4.5)], color='blue', width=5)
s.addNodeCluster("b", [(0,2),(6,6)], color='blue', width=5)
s.addNodeCluster("c", [(4.5,6)], color='blue', width=5)
s.addNodeCluster("d", [(2,2)], color='blue', width=5)

s.addTimeLine(ticks=2)
