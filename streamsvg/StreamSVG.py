# -*- coding: utf-8 -*-
# TODO
# Nettoyage vieux code / Commentaires code
# Documentation
# Remplacer les print(...\n)
# Gestion des erreurs (noeud non ajoute...)

import sys
import svgwrite

def drange(start, stop, step):
    """
        Helper function generating a range of numbers.

        :param start: Range start
        :param end: Range end
        :param step: Range step (the difference between two subsequent elements in the range equals step)
        :type start: float
        :type end: float
        :type step: float
        :return: an iterator over the range
        :rtype: generator

        :Example:

        >>> [i for i in drange(0.0,1.0,0.1)]
        [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    """
    r = start
    while r <= stop:
        yield r
        r += step

class Drawing(object):
    """
        Initializes a stream graph drawing.

        :param alpha: Start time of stream graph.
        :param omega: End time of stream graph.
        :param time_width: Width (in the final fig) of one time unit.
        :param discrete: Duration of the time step if time is discrete. 0 if time is continuous.

        :type alpha: float
        :type omega: float
        :type time_width: positive int
        :type discrete: positive int
        
        :Example:
        
        >>> d = Drawing(alpha=0, omega=5.5)
        >>> d = Drawing(alpha=0, omega=6, discrete=2)
    """

    __version__ = '1.1.1'
    _alpha = 0.0
    _omega = 0.0
    _discrete = -1

    _time_unit = 500
    _node_unit = 12
    _node_sep = _node_unit/4
    
    _num_node_intervals = 0
    #?Is incremented by one if time marks are used too
    _num_time_intervals = 0
    _num_parameters = 0
    _totalval_parameters = 0

    _first_node = ""
    _tick_length = 1
    _tick_width = 1
    _font_size = 10
    _font_family = 'serif'
    _font_color = 'black'
    _mark_size = 2

    _nodes = {}
    _nodes_class = {}
    _node_cpt = 0

    _colors = {}
    _color_cpt = 31
    _directed = False
    _tick_font_family = 'serif'
    _tick_font_size = 5
    _tick_font_color = 'black'
    __add_tm = []

    def __init__(self, name, alpha=0.0, omega=10.0, time_width=5, discrete=0, directed=False):
        #print("""#FIG 3.2  Produced by xfig version 3.2.5b\n\
#Landscape\n\
#Center\n\
#Inches\n\
#Letter\n\
#100.00\n\
#Single\n\
#-2\n\
#1200 2\n""")
#(omega*time_width+15, 1000),
        self.dwg = svgwrite.Drawing(name, debug=True)
        self._alpha = float(alpha)
        self._omega = float(omega)
        self._time_unit = time_width
        self._discrete = discrete
        self._directed = directed

        self._offset_x = self._font_size + self._tick_font_size
        self._offset_y = self._tick_font_size
        self.linetype = 2

        # Useful predefined colors
        self.addColor("grey", "#888888")

    @property
    def arrow_marker(self):
        if not hasattr(self, '_arrow_marker'):
            arrow = self.dwg.marker(id='arrow', insert=(1, 2), size=(10, 10), orient='auto', markerUnits='strokeWidth')
            arrow.add(self.dwg.path(d='M0,0 L0,4 L2,2 z', fill='black'))
            self.dwg.defs.add(arrow)
            self._arrow_marker = arrow
        return self._arrow_marker

    def setLineType(def_linetype):
        """
            Changes the linetype for nodes (i.e. from dashed to dotted). Default is dotted (linetype=2).
            See FIG documentation for all values.

            :param def_linetype: the new linetype
            :type def_linetype: int
        """

        self.linetype = def_linetype

    def addColor(self, name, hex):
        """
            Adds a new RGB color for use.

            :param name: Color identifier (must be unique, case sensitive)
            :param hex: Color in hexadecimal format
            :type name: str
            :type hex: str

            :Example:

            >>> d.addColor("red", "#FF0000")
        """

        self._colors[name] = hex

        #print("0 " + str(self._color_cpt) + " " + str(hex))

    def addNode(self, u, times=[], color=0, linetype=None):
        """
            Adds a new node to the stream graph.

            :param u: Name of the node (should be unique).
            :param times: List of tuples indicating when the node is present.
            :param color: Color of the node, either a XFIG int or a user-defined color.
            :param linetype: ?

            :type u: str
            :type times: list of 2-tuples
            :type color: int or str
        
            :Example:
            
            >>> # Adds a node "v" from alpha to omega
            >>> d.addNode("v")
            >>> # Adds a node "v" from time 1 to time 2.5 and from time 4 to time 8.
            >>> d.addNode("v", times=[(1,2.5),(4,8)])
        """
        if self._discrete > 0:
            self.__addDiscreteNode(u, times, color)
        else:
            self.__addContinuousNode(u, times, color, linetype)

    def __addDiscreteNode(self, u, times=[], color="grey", width=1):

        if color in self._colors:
            color = self._colors[color]

        if self._node_cpt == 1:
            self._first_node = u

        self._node_cpt += 1
        self._nodes[u] = self._node_cpt

        
        print("4 0 " + str(color) + " 50 -1 0 30 0.0000 4 135 120 " + str(self._offset_x + int(self._alpha * self._time_unit) - 400) + " " + str(self._offset_y + 125 + int(self._node_cpt * self._node_unit)) + " " + str(u) + "\\001")

        
        if len(times) == 0:
            for i in drange(self._alpha, self._omega, self._discrete):
                print("1 3 0 " + str(width) + " " + str(color) + " " + str(color) + " 49 -1 20 0.000 1 0.0000 " + str(self._offset_x + int(i * self._time_unit)) + " " + str(self._offset_y + self._nodes[u]*self._node_unit) + " 45 45 -6525 -2025 -6480 -2025")
        else:
            for (i,j) in times:
                for x in drange(i, j, self._discrete):
                    print("1 3 0 " + str(width) + " " + str(color) + " " + str(color) + " 49 -1 20 0.000 1 0.0000 " + str(self._offset_x + int(x * self._time_unit)) + " " + str(self._offset_y + self._nodes[u]*self._node_unit) + " 45 45 -6525 -2025 -6480 -2025")



    def __addContinuousNode(self, u, times=[], color="white", linetype=None):
        """ nodeId : identifiant du noeud
            times : suite d'intervalles de temps ou le noeud est actif
        """

        if linetype is None:
            linetype = self.linetype

        color = self._colors.get(color, "white")

        if self._node_cpt == 1:
            self._first_node = u

        self._node_cpt += 1
        self._nodes[u] = self._node_cpt
        nu = self.dwg.add(self.dwg.g(class_="node_"+u))
        self._nodes_class[u] = nu
        y = (self._node_cpt-1) * (self._node_unit + self._node_sep)
        nu.add(self.dwg.text(str(u), insert=(self._offset_x - self._font_size, self._node_unit/2 + self._font_size/2 - 2 + y + self._offset_y), font_family=self._font_family, font_size=self._font_size, fill=self._font_color))
        nu.add(self.dwg.rect(insert=(self._offset_x, y+self._offset_y), size=(self._omega*self._time_unit, self._node_unit), fill=color))

        if len(times) == 0:
            nu.add(self.dwg.line(start=(+self._offset_x, self._node_unit/2+y+self._offset_y), end=(self._omega*self._time_unit++self._offset_x,  self._node_unit/2+y+self._offset_y), stroke_width="1", stroke_dasharray="1 1", stroke='black'))#(self._omega*self._time_unit)
        else:
            for (i,j) in times:
                nu.add(self.dwg.line(start=(self._offset_x+i*self._time_unit, self._node_unit/2+y+self._offset_y), end=(self._offset_x+j*self._time_unit, self._node_unit/2+y+self._offset_y), stroke_width="1", stroke_dasharray="1 5", stroke='black'))

    def addLink(self, u, v, b, e, curving=0.0, color='black', height=0.5, width=2):
        """
            Adds a link from time b to time e between nodes u and v.

            :param u: Node to be linked
            :param v: Node to be linked
            :param b: Start time of the link
            :param e: End time of the link
            :param curving: Curving of the link. 0 corresponds to a straight link, 
                            negative values will draw the link bent on the left, 
                            positive values will draw the link bent on the right
            :param color: the link's color (see addColor())
            :param height:  Fixes the position of the duration bar; values are between 0 and 1.
                            0 would draw the duration bar at node u's level, 1 at node's v, 0.5 in between, etc.
            :param width: The link's width

            :type u: str
            :type v: str
            :type b: float
            :type e: float
            :type curving: float
            :type color: str/int
            :type height: float
            :type width: int

            :Example:

            >>> # Add link from time 1 to time 3 between nodes u and v
            >>> d.addLink("u", "v", 1, 3)
            >>> # Add a right curved link from time 1 to time 3 between nodes u and v
            >>> d.addLink("u", "v", 1, 3, curving=0.3)
        """
        if self._discrete > 0:
            self.__addDiscreteLink(u, v, b, e, curving, color, height, width)
        else:
            self.__addContinuousLink(u, v, b, e, curving, color, height, width)

    def __addDiscreteLink(self, u, v, b, e, curving=0.0, color=0, height=0.5, width=3):
        if color in self._colors:
            color = self._colors[color]
        if self._directed:
            if self._nodes[u] > self._nodes[v]:
                (u,v) = (v,u)
                arrow_type = "0 1"
            else:
                arrow_type = "1 0"
        else:
            if self._nodes[u] > self._nodes[v]:
                (u,v) = (v,u)
            arrow_type = "0 0"

        for i in drange(b,e, self._discrete):
            pass

    def __addContinuousLink(self, u, v, b, e, curving=0.0, color='black', height=0.5, width=1):
        # Draw circles for u and v
        luv = self.dwg.add(self.dwg.g(class_="link_" + str(u) + "_" + str(v)))
        ucpt = min(self._nodes[u], self._nodes[v])
        vcpt = max(self._nodes[u], self._nodes[v])
        yu = (ucpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 
        yv = (vcpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2
        x_off = b*self._time_unit+self._offset_x
        luv.add(self.dwg.circle(center=(x_off, yu + self._offset_y), r=self._node_unit/5, fill=color))
        luv.add(self.dwg.circle(center=(x_off, yv + self._offset_y), r=self._node_unit/5, fill=color))
        
        xm = (b + curving) * self._time_unit + self._offset_x
        ym = (yu + yv)*height
        if curving > 0.:
            luv.add(self.dwg.path(d=("M" + str(x_off) + " " + str(yu + self._offset_y) +
                                     " Q" + " " + str(xm) + " " + str(ym + self._offset_y) + " " + str(x_off) + " " + str(yv + self._offset_y)),
                                  stroke_width=width,
                                  stroke=color,
                                  fill_opacity="0."))
        else:
            luv.add(self.dwg.line(start=(x_off, yu + self._offset_y), end=(x_off, yv + self._offset_y), stroke_width=width, stroke=color))

        # Duration
        luv.add(self.dwg.line(start=(xm, ym + self._offset_y), end=(e * self._time_unit + self._offset_x, ym + self._offset_y), stroke_width=width, stroke=color))

    def addNodeCluster(self, u, times=[], color='blue', width=None):
        """
            Adds a node cluster (drawn as a rectangle) for one node over time.

            :param u: The node in the cluster
            :param times: The times at which u is in the cluster
            :param color: The color of the rectangle
            :param width: The width of the rectangle

            :type u: str
            :type times: list of tuples
            :type color: str/int
            :type width: int

            :Example:

            >>> # Create the blue node cluster {u}x[3,4] U {v}x[5,7.5] U {x}x[2,4]
            >>> d.addNodeCluster("u", [(3,4)], color=11)
            >>> d.addNodeCluster("v", [(5,7.5)], color=11)
            >>> d.addNodeCluster("x", [(2,4)], color=11)

        """
        if width is None:
            width = 3*self._node_unit/4
        margin = width / 2

        #if color in self._colors:
        #    color = self._colors[color]        

        nu = self._nodes_class[u]
        node_cpt = self._nodes[u]
        y = (node_cpt-1) * (self._node_unit + self._node_sep) + self._offset_y

        if len(times) == 0:
            times = [(self._alpha, self._omega)]

        #width, j-i
        for (i,j) in times:
            nu.add(self.dwg.rect(insert=(self._offset_x + i*self._time_unit, y + self._node_unit/2-margin), size=((j-i)*self._time_unit, width), fill=color, fill_opacity="0.4"))
            
    def addParameter(self, letter, value, color=0, width=1):
        """
            Adds a parameter (like Delta=2). Multiple parameters will be placed at the top of the drawing, on each other's side 

            :param letter: The letter for the parameter, in ascii (will be translated in greek, i.e. d gives delta, m gives mu, etc.)
            :param value: The value for the parameter
            :param color: The color (see addColor())
            :param width: The interval's width

            :type letter: str
            :type value: float
            :type color: int/str
            :type width: int

            :Example:
            
            >>> # Adds a parameter delta with value 3
            >>> d.addParameter("d", 3)
        """

        if color in self._colors:
            color = self._colors[color]

        #?Place at top? Confusing with time intervals...
        pos_segment_y = self._offset_y + (self._nodes[self._first_node] * self._node_unit) - (150 * self._num_time_intervals) - 400
        # Place at bottom instead? Then needs to be written last.
        # pos_segment_y = self._offset_y + self._node_cpt * self._node_unit + 2*self._node_unit

        if self._num_parameters == 0:
            paramoffset = 0
        else:
            paramoffset = 200

        print("2 1 " + str(color) + " " + str(width) + " 0 7 50 -1 -1 0.000 0 0 -1 1 1 2")
        print("13 1 1.00 60.00 120.00")
        print("13 1 1.00 60.00 120.00")
        print(str(self._offset_x + (self._totalval_parameters * self._time_unit  + (self._num_parameters * paramoffset))) + " " + str(pos_segment_y) + " " + str(self._offset_x + int(value * self._time_unit) + (self._totalval_parameters * self._time_unit + (self._num_parameters * paramoffset))) + " " + str(pos_segment_y))

        valtocenter = int(value * self._time_unit / 2) - (200 + (50 * max(int(value) - 2, 0))) 

        print("4 0 0 50 -1 32 14 0.0000 4 180 375 " + str(self._offset_x + (self._totalval_parameters * self._time_unit + int(self._num_parameters * paramoffset)) + valtocenter)  + " " + str(pos_segment_y - 150)  + " " + str(letter) + " = " + str(value) + "\\001")
        self._totalval_parameters += value
        self._num_parameters += 1

    def addNodeIntervalMark(self, u, v, color='black', width=1):
        ucpt = min(self._nodes[u], self._nodes[v])
        vcpt = max(self._nodes[u], self._nodes[v])
        yu = (ucpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 
        yv = (vcpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2
        x_off = self._offset_x/10

        self.dwg.add(self.dwg.line(start=(self._tick_length + x_off, yu + self._offset_y), end=(self._tick_length + x_off, yv + self._offset_y), stroke_width=width, stroke=color))
        self.dwg.add(self.dwg.line(start=(x_off, yu + self._offset_y), end=(2*self._tick_length + x_off, yu + self._offset_y), stroke_width=width, stroke=color))
        self.dwg.add(self.dwg.line(start=(x_off, yv + self._offset_y), end=(2*self._tick_length + x_off, yv + self._offset_y), stroke_width=width, stroke=color))

    def addTimeNodeMark(self, t, v, color='black', width=2, opacity='1.0'):
        """
            Adds a mark (a cross) at a given node and time.

            :param t: The time at which to add the mark
            :param v: The node at which to add the mark
            :param color: The mark's color (see addColor())
            :param width: The mark's width
            :param depth: Layer for XFIG. Higher values will put the mark in the background, lower in the foreground.

            :type t: float
            :type v: str
            :type color: int/str
            :type width: int
            :type depth: int

            :Example:

            >>> d.addTimeNodeMark(2, "u", color=11, width=3)
        """
        cx = (t * self._time_unit) + self._offset_x + 0.5
        cy = (self._nodes[v]-1) * (self._node_unit + self._node_sep) + self._node_unit/2 + self._offset_y
        a = "M " + str(cx - self._mark_size) + "," + str(cy - self._mark_size)
        b = "L " + str(cx + self._mark_size) + "," + str(cy + self._mark_size)
        c = "M " + str(cx + self._mark_size) + "," + str(cy - self._mark_size)
        d = "L " + str(cx - self._mark_size) + "," + str(cy + self._mark_size)
        self.dwg.add(self.dwg.path(d=" ".join([a, b, c, d]),
                                   fill = "none",
                                   stroke_width=width, stroke=color, stroke_opacity=opacity))

    def addPath(self, path, start, end, gamma=0, color='yellow', opacity='0.7', width=1, depth=51):
        """
            Adds a temporal path from a sequence of (t,u,v) meaning that there was a hop from u to v at time t.

            :param path: A list of (t,u,v) that are the hops in the path
            :param start: The start time of the path
            :param end: The end time of the path
            :param gamma: Useful for gamma-path (if gamma > 0, the hops from u to v will take gamma time units)
            :param color: The path's color (see addColor())
            :param width: The path's width
            :param depth: Layer for XFIG. Higher values will put the mark in the background, lower in the foreground.

            :type path: list
            :type start: float
            :type end: float
            :type gamma: float
            :type color: int/str
            :type width: int
            :type depth: int

            :Example:

            >>> # Path from u to x from time 1 to time 9
            >>> d.addPath([(2,u,v), (5, v, x)], 1, 7)
            >>> # gamma=2-path from u to x from time 1 to time 9
            >>> d.addPath([(2,u,v), (5, v, x)], 1, 9, gamma=2)
        """        
        if not len(path):
            return

        x_off = self._offset_x
        t, u, _ = path[0]
        point = []
        if t!=start:
            ucpt = self._nodes[u]
            yu = (ucpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 + self._offset_y
            point.append(((start * self._time_unit) + x_off, yu))

        for tk, u, v in path:
            ucpt = self._nodes[u]
            vcpt = self._nodes[v]
            yu = (ucpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 + self._offset_y
            yv = (vcpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 + self._offset_y
            xu = (tk * self._time_unit) + x_off
            if tk < end:
                xv = (tk * self._time_unit + gamma) + x_off
            else:
                xv = xu
            point.append((xu, yu))
            point.append((xv, yv))
        t, _, v = path[-1]
        vcpt = self._nodes[v]
        yv = (vcpt-1) * (self._node_unit + self._node_sep) + self._node_unit/2 + self._offset_y         
        if t != end:
            point.append(((end * self._time_unit) + x_off, yv))

        self.dwg.add(self.dwg.polyline(point, stroke_width=width, stroke=color, stroke_opacity=opacity, fill_opacity='0'))

    def addRectangle(self, u, v, b, e, width=100, depth=51, opacity='0.5', color='green', border="", bordercolor=None, borderwidth=0):
        """
            Adds a rectangle from node u to node v and from time b to time e.
            The corners of the rectangle will be (u,b), (u,e), (v,b), (v,e)

            :param u: Start node
            :param v: End node
            :param b: Start time
            :param e: End time
            :param width: The rectangle's width (to add an offset)
            :param depth: Layer for XFIG. Higher values will put the mark in the background, lower in the foreground
            :param color: Background color (see addColor())
            :param border: If borders should be drawn, takes "lrtb" (for left, right, top, bottom) as arguments
            :param bordercolor: The border's color (see addColor())
            :param borderwidth: The border's width

            :type u: str
            :type v: str
            :type b: float
            :type e: float
            :type width: int
            :type depth: int
            :type color: int/str
            :type border: str
            :type bordercolor: int/str
            :type borderwidth: int

            :Example:

            >>> # Rectangle without border
            >>> d.addRectangle("u", "v", 2, 6, color=11) 
            >>> # Rectangle with border all around
            >>> d.addRectangle("u", "v", 2, 6, color=11, border="lrtb")
            >>> # Rectangle with borders except on top
            >>> d.addRectangle("u", "v", 2, 6, color=11, border="lrb")
        """

        if bordercolor is None:
            bordercolor = color

        nu = self.dwg.add(self.dwg.g(class_="node_"+u))
        nctu = self._nodes[u]
        nctv = self._nodes[v]
        t_pos = (nctu-1) * (self._node_unit + self._node_sep)
        d_pos = (nctv-1) * (self._node_unit + self._node_sep)
        self.dwg.add(self.dwg.rect(insert=(self._offset_x+b*self._time_unit, t_pos+self._node_unit/2-0.5+self._offset_y), size=((e-b)*self._time_unit, d_pos+1), fill=color, stroke=bordercolor, stroke_width=borderwidth, fill_opacity=opacity))

    def __addTime(self, t, label="", width=1, color='black', opacity=0.8):
        y = (self._node_cpt) * (self._node_unit + self._node_sep) + self._offset_y
        x = t*self._time_unit + 0.5 + self._offset_x
        self.dwg.add(self.dwg.line(start=(x, self._offset_y), end=(x, y), stroke_width=str(width), stroke_dasharray="1 1", stroke='black', stroke_opacity=str(opacity)))
        if label != "" or label is None:
            self.dwg.add(self.dwg.text(str(label), insert=(x-2.0, self._offset_y - 1.0), font_family=self._tick_font_family, font_size=self._tick_font_size))

    def addTime(self, t, label="", width=1, color='black', opacity=0.5):
        """
            Adds a vertical dotted line at a given time.

            :param t: the time at which the line will be drawn
            :param label: the label that will be displayed on top of the vertical line
            :param width: the line's width
            :param font: the label's font (in pt)
            :param color: the line's color (XFIG defined or user-defined, see addColor() )

            :Example:
        
            >>> # Adds a vertical line labelled "t" at time 2
            >>> d.addTime(2, "t")
        """
        self.__add_tm.append(([t], dict(label=label, width=width, color=color, opacity=opacity)))
        
    def addTimeLine(self, ticks=1, marks=None):
        self.__add_tl = dict(ticks=ticks, marks=marks)

    def __addTimeLine(self, ticks=1, marks=None):
        """
            Adds a time line at the bottom of the stream graph.

            /!\ Should be called last /!\

            :param ticks: Granularity a which ticks should be outputted (every 2, every 1, etc.)
            :param marks: Custom ticks in the form (t, l)

            :type ticks: float
            :type marks: list

            :Example:
            
            >>> # Most common usage
            >>> d.addTimeLine(ticks=2)
            >>> # With one custom tick labeled "a" at time 2.5
            >>> d.addTimeLine(ticks=2, marks=[(2.5, "a")])
        """

        vals = []
        i = self._alpha
        while i < self._omega:
            if (i).is_integer():
                vals.append((int(i),int(i)))
            else:
                vals.append((i,i))
            i = i+ticks
        
        if marks is not None:
            # Ajouter/remplacer les valeurs (t, v)
            for (t,v) in marks:
                found = False
                for x in range(0, len(vals)):
                    if vals[x][0] == t:
                        vals[x] = (t,v)
                        found = True
                if not found:
                    vals.append((t,v))

        # Time arrow
        if self._discrete > 0:
            start, end = self._omega - 0.5, self._omega
        else:
            start, end = self._alpha, self._omega

        y = (self._node_cpt) * (self._node_unit + self._node_sep) + self._offset_y

        line = self.dwg.add(self.dwg.line(start=(self._offset_x, y), end=(self._omega*self._time_unit+self._offset_x,  y), stroke_width="1", stroke='black', marker_end=self.arrow_marker.get_funciri()))
        for t, v in vals:
            x = t*self._time_unit + self._offset_x + 0.5
            self.dwg.add(self.dwg.line(start=(x, y), end=(x, y + self._tick_length), stroke_width=str(self._tick_width), stroke='black'))
            self.dwg.add(self.dwg.text(str(v), insert=(x-self._tick_font_size/4 - 0.2, y + self._tick_length + self._tick_font_size - 0.5), font_family=self._tick_font_family, font_size=self._tick_font_size, fill=self._tick_font_color))
        self.dwg.add(self.dwg.text('time', insert=(self._omega*self._time_unit + self._offset_x, y + self._tick_length + self._tick_font_size - 0.5), font_family=self._tick_font_family, font_size=self._tick_font_size*0.8, fill=self._tick_font_color))
        # set marker (start, mid and end markers are the same)

    def __del__(self):
        # Adds white rectangle in background around first node (for EPS bounding box)
        #self.addRectangle(self._first_node, self._first_node, self._alpha, self._omega, width=300,depth=60, color=7)
        pass

    def save(self):
        if hasattr(self, '__add_tl') is not None:
            self.__addTimeLine(**self.__add_tl)
        for args, kargs in self.__add_tm:
            self.__addTime(*args, **kargs) 
        self.dwg.save() 

# main
if __name__ == '__main__':

    # s = Drawing()
    # s = Drawing(alpha=0, omega=10)
    s = Drawing("out.svg", alpha=0, omega=10)

    s.addColor("grey", "#888888")
    s.addColor("red", "#ff0000")

    s.addNode("u")
    s.addNode("v")
    s.addNode("x")
    s.addNode("y", times=[(0.5, 5), (6, 10)])

    s.addNodeCluster("u", [(0.5,2)], width=12)
    s.addNodeCluster("v", color='red')
    s.addRectangle("u", "v", 4, 6, color='green')
    s.addNodeCluster("u", [(6, 7.5)], color="red")

    s.addLink("u", "v", 1.5, 6, curving=0.2)
    s.addLink("v", "x", 3, 5)

    s.addPath([(2, "u", "v"), (4, "v", "x")], 1, 9, width=1)   
    s.addPath([(2, "y", "x")], 1, 4, gamma=0.5, color='pink', width=1)
    s.addLink("u", "v", 1, 4, height=0.4)
    s.addLink("u", "v", 5, 7)
    s.addLink("v", "x", 3, 4)

    s.addTime(4, label="u", width=1, color='black')    
    s.addTimeLine(ticks=2, marks=[(2, "a"), (2.5, "c"), (5, "t"), (6, "b")])
    s.addTimeNodeMark(4, "y", width=0.5)
    s.addNodeIntervalMark("u", "x", color='black')
    s.save()
    #s.save(addTimeLine=dict(ticks=2))
