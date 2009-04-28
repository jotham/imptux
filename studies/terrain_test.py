import pyglet, random, time, math
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
    scale = 1.0
    def __init__ (self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def update (self):
        gl.glColor3f(*self.color)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        gl.glScalef(self.scale, self.scale, self.scale)
        for list in self.vertex_lists:
            list.draw(gl.GL_LINES )
        gl.glPopMatrix()
        
class DroneModel (Model):
    scale = 0.5
    color = (1, 0, 0)
    vertex_lists = [
        pyglet.graphics.vertex_list(6,('v3f/static', (-100, 20.000004, -100, 100, 20.000004, -100, 100, 20.000004, -100, 100, -19.999996, -100, 100, -19.999996, -100, -100, -19.999996, -100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, -19.999996, -100, 100, 20.000004, -100, 100, 20.000004, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, 20.000004, -100, -100, 20.000004, -100, -100, 20.000004, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, 20.000004, -100, -100, -19.999996, -100, -100, -19.999996, -100, 0, -0.000004, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, -19.999996, -100, 100, -19.999996, -100, 100, -19.999996, -100, 0, -0.000004, 100)))
    ]
    
    def update (self, step):
        self.x = 200 * math.sin(step+self.z/200.0)
        Model.update(self)
        
class TerrainModel (Model):
    color = (0.38, 0, 0)
    vertex_lists = [
        pyglet.graphics.vertex_list(2,('v3f/static', (-400, 30, 0, -400, 30, -2000))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-400, 30, -2000, -330, 30, -2000, -330, 30, -2000, -330, 30, 0, -330, 30, 0, -400, 30, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-330, 30, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -330, 30, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -324.956177, 29.579521, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -319.409271, 28.364159, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -310.095367, 25.20192, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -283.322876, 12.78336, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -205.223038, -23.061121, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -160.174072, -38.25024, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -107.280006, -50.640003, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (-56.760002, -57.48, -2000, 0, -60, -2000, 0, -60, -2000, 0, -60, 0, 0, -60, 0, -56.760002, -57.48, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (0, -60, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 0, -60, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 56.400002, -57.48, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 106.000008, -50.640003, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 149.400009, -40.559998, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 194.140793, -25.70784, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 248.400009, -1.68, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 302.198395, 23.825281, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 313.200012, 27.48, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 320.126404, 29.066881, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (323.481598, 29.579521, -2000, 330, 30, -2000, 330, 30, -2000, 330, 30, 0, 330, 30, 0, 323.481598, 29.579521, 0))),
        pyglet.graphics.vertex_list(6,('v3f/static', (330, 30, -2000, 400, 30, -2000, 400, 30, -2000, 400, 30, 0, 400, 30, 0, 330, 30, 0)))
    ]

class Window (pyglet.window.Window):
    def __init__ (self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.camera = Camera()
        self.axis = Axis(40+self.width/-2, 40+self.height/-2, 0)
        self.border = Border(self.width-32, self.height-32)
        self.models = []
        for n in xrange(24):
            self.models.append(DroneModel(n*-100, -100, 000 + n*-110))
        self.terrain = TerrainModel(0,self.height/-4)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glDepthFunc(gl.GL_LEQUAL)
        pyglet.clock.schedule(self.update)
        self.clock = pyglet.clock.ClockDisplay()
        self.step = 0.0
        
    def update (self, dt):
        self.step += 0.01
        
    def on_resize (self, width, height):
        self.camera.defaultView(width, height)
        
    def on_draw (self):
        self.clear()
        self.camera.update()
        self.border.update()
        gl.glEnable(gl.GL_DEPTH_TEST)
        self.axis.update()
        self.terrain.update()
        for model in self.models:
            model.update(self.step)
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
    window = Window(900, 555)
    pyglet.app.run()
    
if __name__ == '__main__':
    main()