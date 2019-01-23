from streamsvg import Drawing

s = Drawing()


s.addNode("a")
s.addNode("b", [(0,4), (5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

s.addLink("a", "b", 1, 3)
s.addLink("b", "d", 2, 3)
s.addLink("a", "c", 4.5, 7.5, height=0.40)
s.addLink("a", "b", 7, 8)
s.addLink("b", "c", 6, 9)

s.addTimeNodeMark(1, "d",color="#FF9896",width=2)
s.addTimeNodeMark(9, "c",color="#FF9896",width=2)
s.addPath([(2,"d","b"), (3,"b","a"), (7.5, "a", "b"), (8, "b", "c")], 2, 8, color='blue', width=3)

s.addTimeLine(ticks=2)

