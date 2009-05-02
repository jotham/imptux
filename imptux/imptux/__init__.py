import pyglet, models
from pyglet import gl
import ctypes


class Camera (object):
    #~ fog_color = ctypes.cast((gl.GLfloat*4)(0,0,0.0,0), ctypes.POINTER(gl.GLfloat))
    
    def __init__ (self):
        self.fieldofview = 60
        self.clipnear = 0.1
        self.clipfar = 8192
        self.x = 0
        self.y = 0
        self.z = 512
        self.rx = 0
        self.ry = 0
        self.rz = 0
        
    def defaultView (self, width, height):
        self.width = width
        self.height = height
        gl.glViewport(0, 0, self.width, self.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.gluPerspective(self.fieldofview, self.width/float(self.height), self.clipnear, self.clipfar)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        # Fog
        #~ gl.glFogi(gl.GL_FOG_MODE, gl.GL_LINEAR)
        #~ gl.glFogfv(gl.GL_FOG_COLOR, self.fog_color)
        #~ gl.glFogf(gl.GL_FOG_DENSITY, 0.35)
        #~ gl.glHint(gl.GL_FOG_HINT, gl.GL_DONT_CARE)
        #~ gl.glFogf(gl.GL_FOG_START, 500.0)
        #~ gl.glFogf(gl.GL_FOG_END, 7300.0)
        #~ gl.glEnable(gl.GL_FOG)
        
    def update (self, dt=0):
        pass
        
    def position (self, target=None):
        gl.glLoadIdentity()
        if target:
            gl.gluLookAt(self.x, self.y, self.z, target[0], target[1], target[2], 0, 1, 0)
        else:
            gl.glTranslatef(-self.x,-self.y,-self.z)
            gl.glRotatef(self.rx,1,0,0)
            gl.glRotatef(self.ry,0,1,0)
            gl.glRotatef(self.rz,0,0,1)
        
class Axis (object):
    def __init__ (self, x=0, y=0, z=0, size=100):
        self.vertex_list = pyglet.graphics.vertex_list(6,
            ('v3f/static', (0,0,0,size,0,0,0,0,0,0,size,0,0,0,0,0,0,size)), 
            ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
        self.x = x
        self.y = y
        self.z = z
        
    def draw (self):
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.vertex_list.draw(gl.GL_LINES)
        gl.glPopMatrix()

class Border (object):
    def __init__ (self, width, height, color=(1.,1.,1.)):
        self.color = color
        points = [0,0,0,0,height,0,0,height,0,width,height,0,width,height,0,width,0,0,width,0,0,0,0,0]
        for n in xrange(len(points)/3):
            points[n*3] += width/-2
            points[n*3+1] += height/-2
        self.vertex_list = pyglet.graphics.vertex_list(8,('v3f/static', points))
            
    def draw (self):
        gl.glColor3f(*self.color)
        self.vertex_list.draw(gl.GL_LINES)
        