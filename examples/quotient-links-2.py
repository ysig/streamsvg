# Dark blue = 10
# Dark green = 12
# Purple = 21
# Pink = 27
from streamsvg import Drawing

s = Drawing()

s.addNode("A", color='green')
s.addNode("B", color='blue')
s.addNode("C", color='orange')
s.addNode("D", color='magenta')

s.addLink("A", "B", 2, 4)
s.addLink("A", "C", 3, 4, height=0.4)
s.addLink("B", "C", 3, 4)
s.addLink("A", "C", 6, 7)
s.addLink("C", "D", 9, 10)

s.addTimeLine(ticks=2)
