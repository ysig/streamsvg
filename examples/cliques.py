from streamsvg import Drawing

sg = Drawing()
sg.addNode("a")
sg.addNode("b")
sg.addNode("c")
sg.addNode("d")

sg.addLink("a", "b", 0, 4)
sg.addLink("a", "b", 6, 9)
sg.addLink("a", "c", 2, 5, height=0.4)
sg.addLink("b", "c", 1, 8)
sg.addLink("b", "d", 7, 10, height=0.4)
sg.addLink("c", "d", 6, 9)

sg.addRectangle("a","c",2,4,color='blue')
sg.addRectangle("b","d",7,8,color="#FF8080")

sg.addTimeLine(ticks=2)

