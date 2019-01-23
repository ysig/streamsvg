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


s.addRectangle("a", "a", 0, .95, color='none', bordercolor="#98DF8A")
s.addRectangle("b", "b", 0, .95, color='none', bordercolor="#98DF8A")

s.addRectangle("a", "b", 1, 1.95, color='none', bordercolor="#98DF8A")
s.addRectangle("d", "d", 1, 1.95, color='none', bordercolor="#98DF8A")

s.addRectangle("a", "d", 2, 3, color='none', bordercolor="#98DF8A")

s.addRectangle("a", "a", 3.05, 4.45, color='none', bordercolor="#98DF8A")
s.addRectangle("b", "b", 3.05, 4, color='none', bordercolor="#98DF8A")
s.addRectangle("c", "c", 4, 4.45, color='none', bordercolor="#98DF8A")

s.addRectangle("a", "c", 4.5, 5.95, color='none', bordercolor="#98DF8A")
s.addRectangle("b", "b", 5, 5.95, color='none', bordercolor="#98DF8A")

s.addRectangle("a", "c", 6, 8, color='none', bordercolor="#98DF8A")
s.addRectangle("a", "a", 8.05, 10, color='none', bordercolor="#98DF8A")
s.addRectangle("b", "c", 8.05, 9, color='none', bordercolor="#98DF8A")
s.addRectangle("b", "b", 9.05, 10, color='none', bordercolor="#98DF8A")


s.addTimeLine(ticks=2)

