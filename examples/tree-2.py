from streamsvg import Drawing

s = Drawing()

s.addNode("a")
s.addNode("b", [(0,4), (5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

s.addLink("a", "b", 2, 2, color='blue', width=3)
s.addLink("b", "d", 2, 2, color='blue', width=3)
s.addLink("a", "c", 5, 5, color='blue', width=3)
s.addLink("b", "c", 6, 6, color='blue', width=3)
s.addLink("b", "c", 7, 7, color='blue', width=3)
s.addLink("b", "c", 8, 8, color='blue', width=3)
s.addLink("a", "b", 8, 8, color='blue', width=3)

s.addLink("a", "b", 1, 3)
s.addLink("b", "d", 2, 3)
s.addLink("a", "c", 4.5, 7.5, height=0.40)
s.addLink("a", "b", 7, 8)
s.addLink("b", "c", 6, 9)

s.addTimeNodeMark(2, "b", color="#FF9896", width=2)

s.addNodeCluster("a", [(2,6),(8,9)], color='blue', width=5)
s.addNodeCluster("b", [(6,7),(8,10)], color='blue', width=5)
s.addNodeCluster("c", [(5,6),(7,9)], color='blue', width=5)
s.addNodeCluster("d", [(2,3)], color='blue', width=5)

s.addTimeLine(ticks=2)
