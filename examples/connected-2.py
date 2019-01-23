from streamsvg import Drawing

s = Drawing()

s.addNode("a", [(0,10)])
s.addNode("b", [(0,4),(5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

s.addLink("a","b",1,3)
s.addLink("a","b",7,8)
s.addLink("b","c",6,9)
s.addLink("b","d",2,3,height=0.4)
s.addLink("a","c",4.5,7.5,height=0.4)

s.addNodeCluster("a", [(0,10)], color='blue',width=5)
s.addNodeCluster("a", [(1,3)], color='blue',width=7)
s.addNodeCluster("b", [(7,8)], color='blue',width=5)
s.addNodeCluster("b", [(1,3)], color='blue',width=7)
s.addNodeCluster("c", [(7,8)], color='blue',width=5)
s.addNodeCluster("d", [(2,3)], color='blue',width=7)

# $[2,3]\times\{a,b,d\} \cup [1,2]\times\{a,b\} \cup [0,10]\times\{a\} \cup [7,8]\times\{a,b,c\}$
# $[2,3]\times\{a,b,d\} \cup [1,2]\times\{a,b\} \cup [0,4]\times\{b\}$

s.addNodeCluster("a", [(1,3)], color='#FF9896',width=5)
s.addNodeCluster("b", [(0,4)], color='#FF9896',width=5)
s.addNodeCluster("d", [(2,3)], color='#FF9896',width=5)

s.addTimeLine(ticks=2)
