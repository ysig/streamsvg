from streamsvg import Drawing

s = Drawing()

s.addNode("a", [(0,10)])
s.addNode("b", [(0,4),(5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

s.addLink("a","b",1,3,width=3)
s.addLink("a","b",7,8,width=3)
s.addLink("b","c",6,9,color="#BBBBBB",width=2)
s.addLink("b","d",2,3,height=0.4,color="#BBBBBB",width=2)
s.addLink("a","c",4.5,7.5,height=0.4,width=3)

s.addNodeCluster("b",[(1,3),(7,8)],color="blue",width=3)
s.addNodeCluster("c",[(4.5,7.5)],color="blue",width=3)

s.addTimeLine(ticks=2)

