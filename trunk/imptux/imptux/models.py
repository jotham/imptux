import math, pyglet

class Model (object):
    scale = 1.
    color = (1.,1.,1.)
    def __init__ (self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def draw (self):
        gl.glColor3f(*self.color)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        gl.glScalef(self.scale, self.scale, self.scale)
        for list in self.vertex_lists:
            list.draw(gl.GL_LINES)
        gl.glPopMatrix()
        
class TerrainModel (Model):
    color = (0.38, 0, 0)
    vertex_lists = [
        pyglet.graphics.vertex_list(8,('v3f/static', (-400, 30, -2000, -330, 30, -2000, -330, 30, -2000, -330, 30, 0, -330, 30, 0, -400, 30, 0, -400, 30, 0, -400, 30, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-330, 30, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -330, 30, 0, -330, 30, 0, -330, 30, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (-56.760002, -57.48, -2000, 0, -60, -2000, 0, -60, -2000, 0, -60, 0, 0, -60, 0, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -56.760002, -57.48, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (0, -60, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 0, -60, 0, 0, -60, 0, 0, -60, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 56.400002, -57.48, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 248.400009, -1.68, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 313.200012, 27.48, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (323.481598, 29.579521, -2000, 330, 30, -2000, 330, 30, -2000, 330, 30, 0, 330, 30, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, -2000))),
        pyglet.graphics.vertex_list(8,('v3f/static', (330, 30, -2000, 400, 30, -2000, 400, 30, -2000, 400, 30, 0, 400, 30, 0, 330, 30, 0, 330, 30, 0, 330, 30, -2000))),
    ]
    
class TerrainCage (Model):
    color = (1, 0, 1)
    def __init__ (self, *args, **kwargs):
        super(TerrainCage, self).__init__(*args, **kwargs)
        temp = []
        segments = 32
        first = last = None
        for n in xrange(segments):
            a = math.pi*1.32 + n/float(segments) * math.pi/2.7
            x = 600 * math.cos(a)
            y = 600 * math.sin(a) + 400
            if last:
                temp.extend([last[0], last[1], 0, x, y, 0])
            else:
                first = (x, y, 0)
            last = (x, y, 0)
        temp.extend([last[0], last[1], 0, first[0], first[1], 0])
        self.vertex_lists = [pyglet.graphics.vertex_list(segments*2, ('v3f/static', temp))]
            
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
        super(DroneModel, self).update()

class PlayerBulletModel (Model):
    color = (1, 1, 0)
    vertex_lists = [
        pyglet.graphics.vertex_list(6, ('v3f/static', (-10, 0, 5, 0, 0, -5, 0, 0, -5, 10, 0, 5, 10, 0, 5, -10, 0, 5)))
    ]
    
    def __init__ (self, *args, **kwargs):
        super(PlayerBulletModel, self).__init__(*args, **kwargs)
        self.vz = -15
        #~ self.decay = 1
        #~ self.fire_delay = .25
        #~ self.timestamp = 0
        
    def update (self, step):
        #self.x = 200 * math.sin(step+self.z/200.0)
        self.z = self.z + self.vz
        # self.vx *= self.decay
        super(PlayerBulletModel, self).update()
    
class PlayerDroneModel (Model):
    scale = 0.5
    color = (0, 1, 0)
    vertex_lists = [
        pyglet.graphics.vertex_list(6,('v3f/static', (-100, 20.000004, 100, 100, 20.000004, 100, 100, 20.000004, 100, 100, -19.999996, 100, 100, -19.999996, 100, -100, -19.999996, 100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, -19.999996, 100, 100, 20.000004, 100, 100, 20.000004, 100, 0, -0.000004, -100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (100, 20.000004, 100, -100, 20.000004, 100, -100, 20.000004, 100, 0, -0.000004, -100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, 20.000004, 100, -100, -19.999996, 100, -100, -19.999996, 100, 0, -0.000004, -100))),
        pyglet.graphics.vertex_list(4,('v3f/static', (-100, -19.999996, 100, 100, -19.999996, 100, 100, -19.999996, 100, 0, -0.000004, -100)))
    ]
    
    def __init__ (self, *args, **kwargs):
        super(PlayerDroneModel, self).__init__(*args, **kwargs)
        self.vx = 0
        self.decay = 1
        self.fire_delay = .25
        self.timestamp = 0
        
    def update (self, step):
        #self.x = 200 * math.sin(step+self.z/200.0)
        self.x = max(-200, min(200, self.x + self.vx))
        self.vx *= self.decay
        super(PlayerDroneModel, self).update()
        
    def move_left (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = -5
        elif self.vx < 0:
            self.decay = 0.9
            
    def move_right (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = 5
        elif self.vx > 0:
            self.decay = 0.9
        
    def fire (self, now):
        if now > self.timestamp:
            self.timestamp = now + self.fire_delay
            return (PlayerBulletModel(self.x-40, self.y, self.z-18), PlayerBulletModel(self.x+40, self.y, self.z-18))
        return None