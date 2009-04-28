import pyglet, random
from pyglet import gl

class Camera (object):
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
        
    def update(self):
        gl.glLoadIdentity()
        gl.glTranslatef(-self.x,-self.y,-self.z)
        gl.glRotatef(self.rx,1,0,0)
        gl.glRotatef(self.ry,0,1,0)
        gl.glRotatef(self.rz,0,0,1)

class Axis (object):
    def __init__ (self, x=0, y=0, z=0, size=100):
        self.vertex_list = pyglet.graphics.vertex_list(6,
            ('v3f/static', (0,0,0,size,0,0,0,0,0,0,size,0,0,0,0,0,0,size)), 
            ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
        self.ry = 0
        self.ryv = 0
        self.x = x
        self.y = y
        self.z = z
        
    def update (self):
        self.ry += self.ryv
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        gl.glRotatef(self.ry,0,1,0)
        self.vertex_list.draw(gl.GL_LINES)
        gl.glPopMatrix()

class Border (object):
    def __init__ (self, width, height, color=(255,255,255)):
        points = [0,0,0,0,height,0,0,height,0,width,height,0,width,height,0,width,0,0,width,0,0,0,0,0]
        for n in xrange(len(points)/3):
            points[n*3] += width/-2
            points[n*3+1] += height/-2
        self.vertex_list = pyglet.graphics.vertex_list(8,
            ('v3f/static', points),
            ('c3B/static', color*8))
            
    def update (self):
        self.vertex_list.draw(gl.GL_LINES)

class Model (object):
    def __init__ (self, x=0, y=0, z=0, color=(255,0,0)):
        self.x = x
        self.y = y
        self.z = z
        self.zv = random.randrange(1,5)
        self.color = color
        
    def update (self):
        self.z += self.zv
        gl.glPushMatrix()
        gl.glColor3f(*self.color)
        gl.glTranslatef(self.x, self.y, self.z)
        for list in self.vertex_lists:
            list.draw(gl.GL_LINES)
        gl.glPopMatrix()
        
class DroneModel (Model):
    vertex_lists = [
        pyglet.graphics.vertex_list(6,('v3f/static', (-100, 20.000004, -100, 100, 20.000004, -100, 100, 20.000004, -100, 100, -19.999996, -100, 100, -19.999996, -100, -100, -19.999996, -100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, -19.999996, -100, 100, 20.000004, -100, 100, 20.000004, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, 20.000004, -100, -100, 20.000004, -100, -100, 20.000004, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, 20.000004, -100, -100, -19.999996, -100, -100, -19.999996, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, -19.999996, -100, 100, -19.999996, -100, 100, -19.999996, -100, 0, -0.000004, 100)))
    ]
    
class Window (pyglet.window.Window):
    def __init__ (self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.camera = Camera()
        self.axis = Axis(40+self.width/-2, 40+self.height/-2, 0)
        self.border = Border(self.width-32, self.height-32)
        self.models = [
            DroneModel(
                random.randrange(self.width/-2, self.width/2),
                random.randrange(self.width/-2, self.width/2),
                random.randrange(self.width/-2, self.width/2)-2000) for n in xrange(50)]
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glDepthFunc(gl.GL_LEQUAL)
        pyglet.clock.schedule(self.update)
        self.clock = pyglet.clock.ClockDisplay()
        
    def update (self, dt):
        pass
        
    def on_resize (self, width, height):
        self.camera.defaultView(width, height)
        
    def on_draw (self):
        self.clear()
        self.camera.update()
        self.border.update()
        gl.glEnable(gl.GL_DEPTH_TEST)
        self.axis.update()
        for model in self.models:
            model.update()
        gl.glDisable(gl.GL_DEPTH_TEST)
        gl.glTranslatef(self.width/2-160, self.height/-2+20, 0)
        self.clock.draw()
        
    def on_mouse_drag (self, x, y, dx, dy, button, modifiers):
        if button==1:
            self.camera.x-=dx*2
            self.camera.y-=dy*2
        elif button==2:
            self.camera.x-=dx*2
            self.camera.z-=dy*2
        elif button==4:
            self.camera.ry+=dx/4.
            self.camera.rx-=dy/4.
       
def main ():
    window = Window(800, 600)
    pyglet.app.run()
    
if __name__ == '__main__':
    main()