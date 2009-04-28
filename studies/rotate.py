# About OpenGL Projections
#---------------------------------
from pyglet import window,image
from pyglet.window import key
from pyglet.gl import *
import pyglet

class camera():
    x,y,z=0,0,512
    rx,ry,rz=30,-45,0
    w,h=640,480
    far=8192
    fov=60
           
    def view(self,width,height):
        self.w,self.h=width,height
        glViewport(0, 0, width, height)
        self.perspective()

    def perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, float(self.w)/self.h, 0.1, self.far)
        glMatrixMode(GL_MODELVIEW)
       
    def drag(self, x, y, dx, dy, button, modifiers):
        if button==1:
            self.x-=dx*2
            self.y-=dy*2
        elif button==2:
            self.x-=dx*2
            self.z-=dy*2
        elif button==4:
            self.ry+=dx/4.
            self.rx-=dy/4.
       
    def apply(self):
        glLoadIdentity()
        glTranslatef(-self.x,-self.y,-self.z)
        glRotatef(self.rx,1,0,0)
        glRotatef(self.ry,0,1,0)
        glRotatef(self.rz,0,0,1)
    
class Triangle (object):
    def __init__ (self, width, height, color=(255,255,255)):
        self.vertex_list = pyglet.graphics.vertex_list(6,
            ('v3f/static', (-width, 0, 0, 0, height, 0, 0, height, 0, width, 0, 0, width, 0, 0, -width, 0, 0)), 
            ('c3B/static', color*6))
        self.rx = 0
    
    def update (self):
        gl.glTranslatef(200,100,0)
        gl.glRotatef(self.rx,1,0,0)
        self.vertex_list.draw(gl.GL_LINES)
        self.rx += 1
        
class Window (pyglet.window.Window):
    def __init__ (self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDepthFunc(GL_LEQUAL)
        self.camera = camera()
        self.triangle = Triangle(100, 100, (255,0,0))
        pyglet.clock.schedule(self.update)
        
    def update (self, dt):
        pass
        
    def on_resize (self, width, height):
        self.camera.view(width, height)
    
    def on_mouse_drag (self, *args):
        self.camera.drag(*args)

    def on_draw (self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.apply()
        self.triangle.update()
        
        #~ twidth = 100
        #~ theight = 100
        #~ tcolor = (255,0,0)
        #~ vertex_list = pyglet.graphics.vertex_list(6,
            #~ ('v3f/static', (-twidth, 0, 0, 0, theight, 0, 0, theight, 0, twidth, 0, 0, twidth, 0, 0, -twidth, 0, 0)), 
            #~ ('c3B/static', tcolor*6))
        #~ gl.glRotatef(self.rx, 1, 0, 0)
        #~ self.rx += 1
        #~ vertex_list.draw(GL_LINES)
        
window = Window(800, 600)
pyglet.app.run()
