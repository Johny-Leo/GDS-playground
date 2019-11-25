import numpy as np
import gdspy
from gdsCAD import *
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath

import fonts
from fonts import *

a=core.Boundary([[(0.0,0.0),(1.0,0.0),(1.0,1.0),(0.0,1.0)],[(0.0,0.0),(0.5,0.0),(0.5,0.5),(0.0,0.5)]], layer=1)
b=gdspy.PolygonSet([[(0.0,0.0),(2.0,0.0),(2.0,2.0),(0.0,2.0)],[(0.0,0.0),(3.0,0.0),(3.0,3.0),(0.0,3.0)]], layer=1)
c=gdspy.PolygonSet(a.points, layer=1)
d=core.Boundary(b.polygons, layer=1)

def cadply(ply, ly):
    return gdspy.Polygon([list(i) for i in ply], layer=ly)
#end
def pypol2bdy(plst, ly):
    return core.Boundary(plst.polygons, layer=ly)
#end
e=gdspy.boolean(cadply(c.polygons[0],1), cadply(c.polygons[1],1), 'not')
# print(map(tuple, e.polygons[0]))

f=gdspy.boolean(gdspy.Polygon(b.polygons[1]), gdspy.Polygon(b.polygons[0]), 'not')

cl_cad = core.Cell('gdsCAD')
ly_cad = core.Layout('gdsCAD')

cl_cad.add(core.Boundary(map(tuple, e.polygons[0]), layer=1))
# cl_cad.add(d)
ly_cad.add(cl_cad)
ly_cad.save('boolean_test_gdsCAD.gds')

cl_py= gdspy.Cell('gdspy')
# cl_py.add(b)
cl_py.add(f)
cl_py.add(e)
gdspy.write_gds('boolean_test_gdspy.gds',cells=[cl_py])
