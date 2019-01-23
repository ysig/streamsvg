from streamsvg import Drawing

sg = Drawing(alpha=0, omega=4)

sg.addNode("u")
sg.addNode("v")
sg.addNode("w")

sg.addLink("u", "v", 1, 2)
sg.addLink("v", "w", 2, 3)

sg.addPath(((2,"u","v"), (2,"v","w")), 2, 2, color='blue', width=2)

sg.addTimeLine()
