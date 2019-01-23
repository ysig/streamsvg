from streamsvg import Drawing

s = Drawing(alpha=0, omega=8)

s.addNode("u")
s.addNode("x")
s.addNode("v")
s.addNode("y")
s.addNode("w")

s.addLink("u", "x", 0, 1)
s.addLink("x", "v", 2, 4)
s.addLink("v", "y", 3, 5)
s.addLink("y", "w", 6, 7)

#s.addTime(0, label="a")
#s.addTime(1, label="a'")
#s.addTime(2, label="b")
#s.addTime(3, label="c")
#s.addTime(3.5, label="t", color="red")
#s.addTime(4, label="d")
#s.addTime(5, label="e")
#s.addTime(6, label="f'")
#s.addTime(7, label="f")

s.addPath(((1,"u","x"), (2.5,"x","v"), (4.5, "v", "y"), (6, "y", "w")), 1, 6, color='blue', width=2)
s.addTimeNodeMark(3.5,"v",color="#FF0000",width=1)

s.addTimeLine(ticks=2)
