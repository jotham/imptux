#!which `python`

import imptux, pyglet, time, math, random, platform, os
from pyglet import gl
from distutils.version import LooseVersion

GPROFILER_ERROR = None
try:
    from imptux import profiler
except ImportError, e:
    GPROFILER_ERROR = e

# generate displacement map for terrain cage
displacement_resolution = 1024
displacement_resolution_ = displacement_resolution - 1
displacement_map = []
for n in xrange(displacement_resolution):
    angle = math.pi * 1.33 + n/float(displacement_resolution) * math.pi/2.9
    displacement_map.append(((angle-math.pi/2)*180/math.pi, 600*math.cos(angle), 600*math.sin(angle)+358))
def get_displacement (n):
    set = int(((n + 220) / 440.0)*displacement_resolution_)
    return displacement_map[set][0], displacement_map[set][1], displacement_map[set][2]

def prepare (xo,yo,zo,xs,ys,zs,v):
    return_list = []
    for n in xrange(len(v)/3):
        return_list.extend([xo+v[n*3]*xs,yo+v[n*3+1]*ys,zo+v[n*3+2]*zs])
    return return_list

PLAYER_VERTEX_LIST = (-50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, -50.0, 10.000002, 0.0, 50.0, -9.999998, 0.0, 50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, 50.0, -9.999998, 0.0, 50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, 50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, -50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, -50.0, 10.000002, 0.0, -50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, -50.0, -9.999998, 0.0)
TERRAIN_VERTEX_LIST = (-400, 30, -2000, -330, 30, -2000, -330, 30, -2000, -330, 30, 0, -330, 30, 0, -400, 30, 0, -400, 30, 0, -400, 30, -2000, -330, 30, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -330, 30, 0, -330, 30, 0, -330, 30, -2000, -324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, 0, -60, -2000, 0, -60, -2000, 0, -60, 0, 0, -60, 0, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -56.760002, -57.48, -2000, 0, -60, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 0, -60, 0, 0, -60, 0, 0, -60, -2000, 56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 330, 30, -2000, 330, 30, -2000, 330, 30, 0, 330, 30, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, -2000, 330, 30, -2000, 400, 30, -2000, 400, 30, -2000, 400, 30, 0, 400, 30, 0, 330, 30, 0, 330, 30, 0, 330, 30, -2000)
TERRAIN_VERTEX_LIST_2 = prepare(0,0,500,2,2,4,imptux.models.MODEL_CAGE)
ENEMY_VERTEX_LIST = (-50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, -50.0, 10.000002, -100.0, 50.0, -9.999998, -100.0, 50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, 50.0, -9.999998, -100.0, 50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, 50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, -50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, -50.0, 10.000002, -100.0, -50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, -50.0, -9.999998, -100.0)
PLAYER_BULLET_VERTEX_LIST = (-10, 0, 5, 0, 0, -5, 0, 0, -5, 10, 0, 5, 10, 0, 5, -10, 0, 5)
PILLAR_PAIR = prepare(-300,30,0,1,1,1,imptux.models.MODEL_PILLAR)
PILLAR_PAIR.extend(prepare(300,30,0,-1,1,1,imptux.models.MODEL_PILLAR))
PLAYER_SHIP_2 = prepare(0,0,0,0.25,-0.25,-0.25,imptux.models.MODEL_SHIP)

class Terrain (object):
    model = pyglet.graphics.vertex_list(168,('v3f/static', prepare(0,0,0,1,1,4,TERRAIN_VERTEX_LIST)))
    #~ model = pyglet.graphics.vertex_list(320,('v3f/static', TERRAIN_VERTEX_LIST_2))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        pillar_count = 8
        spacing = 800
        self.pillars = [TerrainPillarPair(0,-200,n*-spacing, -spacing*pillar_count) for n in xrange(pillar_count)]
        
    def update (self, dt):
        for pillar in self.pillars:
            pillar.update(dt)
        return True
    
    def draw (self):
        gl.glColor3f(0.38, 0, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
        for pillar in self.pillars:
            pillar.draw()

class TerrainPillarPair (object):
    model = pyglet.graphics.vertex_list(312*2,('v3f/static', PILLAR_PAIR))
    
    def __init__ (self, x, y, z, boundsz):
        self.x = x
        self.y = y
        self.z = z
        self.vz = 2000
        self.boundsz = boundsz
        self.hidden = random.random() < 0.5
        
    def update (self, dt):
        self.z += self.vz * dt
        if self.z >= 0:
            self.z = self.boundsz+self.z
            self.hidden = random.random() < 0.5
        return True
    
    def draw (self):
        if self.hidden: return
        gl.glColor3f(0.38, 0, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()

class Player (object):
    #~ model = pyglet.graphics.vertex_list(32,('v3f/static', prepare(0,0,0,0.5,0.5,0.5, PLAYER_VERTEX_LIST)))
    model = pyglet.graphics.vertex_list(164,('v3f/static', PLAYER_SHIP_2))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.yoffset = 0
        self.decay = 1
        self.iv = 550
        self.fire_delay = .125
        self.timestamp = 0
        self.c = 0
        self.boundsx = 200
        self.bounce_rate = 9
        self.bounce = 0
        self.update()
        
    def draw (self):
        #~ gl.glColor3f(0.2*self.c, 0.6+.4*self.c, 0.2*self.c)
        #~ self.c *= .9
        gl.glColor3f(0.2, 0.7, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.virtual_x, self.virtual_y+self.yoffset, self.z)
        gl.glRotatef(self.virtual_rz,0,0,1)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
    
    def update (self, dt=0):
        self.x = max(-self.boundsx, min(self.boundsx, self.x + (self.vx * dt) ))
        self.vx *= self.decay
        self.yoffset = 4*math.sin(self.bounce)
        self.bounce += self.bounce_rate * dt
        self.virtual_rz, self.virtual_x, self.virtual_y = get_displacement(self.x)
        return True
        
    def move_left (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = -self.iv
        elif self.vx < 0:
            self.decay = 0.8
            
    def move_right (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = self.iv
        elif self.vx > 0:
            self.decay = 0.8
        
    def fire (self, now):
        if True: # now > self.timestamp:
            self.timestamp = now + self.fire_delay
            #~ self.c = 1
            return (PlayerBulletModel(self.x-12, self.y, self.z+5, 5),PlayerBulletModel(self.x+12, self.y, self.z+5, -5))
        return None

class EnemyDrone (object):
    model = pyglet.graphics.vertex_list(32,('v3f/static', prepare(0,0,0,0.5,0.5,0.5,ENEMY_VERTEX_LIST)))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.rz = 0
        self.vz = 400
        self.health = 2
        self.step = 0
        self.step_rate = math.pi/4
        self.c = 0
        self.update()
        
    def update (self, dt=0):
        if self.health < 0 or self.z > 0:
            return False
        self.step += self.step_rate * dt
        self.x = 200 * math.sin(self.step+self.z/200.0)
        self.z += self.vz * dt
        self.left = self.x - 25 # 50
        self.right = self.x + 25 # 50
        self.top = self.z + 0
        self.bottom = self.z - 50 # 100
        self.c *= .9
        self.virtual_rz, self.virtual_x, self.virtual_y = get_displacement(self.x)
        return True
    
    def draw (self):
        #~ gl.glColor3f(1.0, 0, 1.0)
        #~ pyglet.graphics.vertex_list(8, ('v3f/static', (
            #~ self.left, self.y, self.bottom, self.left, self.y, self.top, self.left, self.y,
            #~ self.top, self.right, self.y, self.top, self.right, self.y, self.top, self.right, self.y,
            #~ self.bottom, self.right, self.y, self.bottom, self.left, self.y, self.bottom))).draw(gl.GL_LINES)
        gl.glPushMatrix()
        gl.glTranslatef(self.virtual_x, self.virtual_y, self.z)
        gl.glRotatef(self.virtual_rz,0,0,1)
        gl.glColor3f(1.0, self.c, 0)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
        
    def collision (self, munition):
        #~ if munition.x < self.x:
            #~ self.rz =
        self.c = 1
        self.health -= 1
        
class PlayerBulletModel (object):
    model = pyglet.graphics.vertex_list(6, ('v3f/static', prepare(0,0,0,0.5,0.5,0.5,PLAYER_BULLET_VERTEX_LIST)))
    
    def __init__ (self, x, y, z, vx=0, vz=-650):
        self.x = x
        self.y = y
        self.z = z
        self.rz = 0
        self.vrz = 0
        self.vz = vz
        self.vx = vx
        self.boundsz = -2000
        self.active = True
        self.update()
        
    def update (self, dt=0):
        if not self.active or self.z < self.boundsz or self.x < -200 or self.x > 200:
            return False
        self.z += self.vz * dt
        self.x += self.vx * dt
        self.left = self.x - 5#10
        self.right = self.x + 5#10
        self.top = self.z + 2.5#5
        self.bottom = self.z - 2.5#5
        self.rz += self.vrz * dt
        self.virtual_rz, self.virtual_x, self.virtual_y = get_displacement(self.x)
        return True
    
    def collision (self, entity):
        self.active = False
        
    def draw (self):
        #~ gl.glColor3f(1.0, 0, 1.0)
        #~ pyglet.graphics.vertex_list(8, ('v3f/static', (
            #~ self.left, self.y, self.bottom, self.left, self.y, self.top, self.left, self.y,
            #~ self.top, self.right, self.y, self.top, self.right, self.y, self.top, self.right, self.y,
            #~ self.bottom, self.right, self.y, self.bottom, self.left, self.y, self.bottom))).draw(gl.GL_LINES)
        gl.glColor3f(1, 0.8, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.virtual_x, self.virtual_y, self.z)
        gl.glRotatef(self.virtual_rz+self.rz,0,0,1)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()

class GameScene (object):
    def __init__ (self, window, framerate=60.0):
        self.window = window
        self.width = window.width
        self.height = window.height
        self.framerate = framerate
        self.window.push_handlers(self)
        self.camera = imptux.Camera()
        
        self.window.set_exclusive_mouse()
        #~ self.camera.x, self.camera.y, self.camera.z = (39.1404673467, -128, 76)
        #~ self.camera.rx, self.camera.ry = (-18.75, -22.0)
        #~ self.camera.x, self.camera.y, self.camera.z = (-64.9041492903, -156, 104)
        #~ self.camera.rx, self.camera.ry = (-13.25, -22.5)
        #~ self.camera.x, self.camera.y, self.camera.z = (-19.0407210842, -156, 34)
        #~ self.camera.rx, self.camera.ry = (-13.25, -22.5)
        self.camera.x, self.camera.y, self.camera.z = (-4.29767643203, -178, 34)
        self.camera.rx, self.camera.ry = (-13.25, -22.5)
        self.camera.clipfar = 7000
        self.camera.fieldofview = 90

        self.score = 0
        self.current_font = 0
        
        pyglet.font.add_file(os.path.join('.','imptux', 'l25a__.TTF'))
        self.font = pyglet.font.load('Logic twenty-five A')
        self.score_label = pyglet.text.Label("00000000", 'Logic twenty-five A', 64, color=(200,00,0,255))
        
        #~ self.clock = pyglet.clock.ClockDisplay()
        self.new_game()
        
    def end (self):
        pyglet.clock.unschedule(self.update_game)
        pyglet.clock.unschedule(self.dispatch_enemy)
        self.window.pop_handlers()
        
    def new_game (self):
        pyglet.clock.unschedule(self.update_game)
        pyglet.clock.unschedule(self.dispatch_enemy)
        self.collision_entities = []
        self.munitions = []
        self.terrain = Terrain(0, -200, 0)
        self.player = Player(0, 0, -100)
        pyglet.clock.schedule_interval(self.update_game, 1/self.framerate) 
        pyglet.clock.schedule_interval(self.dispatch_enemy, 2)
        self.dispatch_enemy(0)
        
    def dispatch_enemy (self, dt):
        for n in xrange(4):
            self.collision_entities.append(EnemyDrone(n*-100, -200, -2000 + n*-110))
        
    def update_game (self, dt):
        self.score += 0.5
        self.score_label.text = "%08d" % self.score
        self.player.update(dt)
        self.terrain.update(dt)
        temp = []
        for entity in self.collision_entities:
            if entity.update(dt):
                temp.append(entity)
            else: # TODO: Fix this score hack
                self.score += 100
                self.score_label.text = "%08d" % self.score
        self.collision_entities = temp
        temp = []
        for munition in self.munitions:
            if munition.update(dt):
                # TODO: Maybe dispose of the munition automatically upon collision?
                temp.append(munition)
                for entity in self.collision_entities:
                    if entity.left <= munition.right and munition.left <= entity.right and entity.bottom <= munition.top and munition.bottom <= entity.top:
                        entity.collision(munition)
                        munition.collision(entity)
                        break
        self.munitions = temp
        self.camera.update()
        self.window.invalid = True
        
    def player_fire (self):
        munition_objects = self.player.fire(time.time())
        if munition_objects:
            self.munitions.extend(munition_objects)
                
    def on_draw (self):
        self.window.clear()
        self.camera.x = self.player.x/1.5
        self.camera.position((0, 0, -10000))
        rz = self.player.x / 200.0
        gl.glRotatef(-5*rz,0,0,1)
        self.terrain.draw()
        gl.glEnable(gl.GL_DEPTH_TEST)
        for entity in self.collision_entities:
            entity.draw()
        for munition in self.munitions:
            munition.draw()
        gl.glDisable(gl.GL_DEPTH_TEST)
        self.player.draw()
        # Draw UI
        gl.glLoadIdentity()
        if self.window.fullscreen:
            gl.glTranslatef(self.width-self.score_label.content_width,self.height-self.score_label.content_height,-1100)
        else:
            gl.glTranslatef(self.width-self.score_label.content_width,self.height-self.score_label.content_height,-512)
        self.score_label.draw()
        self.window.invalid = False
        
    def on_key_press (self, symbol, modifiers):
        if symbol == pyglet.window.key.A:
            self.player.move_left(1)
        elif symbol == pyglet.window.key.D:
            self.player.move_right(1)
        elif symbol == pyglet.window.key.R:
            self.current_font = (self.current_font - 1) % len(font_list)
            print 'Font: ' + font_list[self.current_font][1]
            self.set_ui_font()
        elif symbol == pyglet.window.key.T:
            self.current_font = (self.current_font + 1) % len(font_list)
            print 'Font: ' + font_list[self.current_font][1]
            self.set_ui_font()
        
    def on_key_release (self, symbol, modifiers):
        if symbol == pyglet.window.key.A:
            self.player.move_left(0)
        elif symbol == pyglet.window.key.D:
            self.player.move_right(0)
        elif symbol == pyglet.window.key.SPACE:
            self.player_fire()
        elif symbol == pyglet.window.key.C:
            print 'self.camera.x, self.camera.y, self.camera.z = (%s, %s, %s)' % (self.camera.x, self.camera.y, self.camera.z)
            print 'self.camera.rx, self.camera.ry = (%s, %s)' % (self.camera.rx, self.camera.ry)
        
    def on_mouse_press (self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            self.player_fire()
    
    def on_resize (self, width, height):
        self.width = width
        self.height = height
        self.camera.defaultView(width, height)
        self.window.invalid = True
        return pyglet.event.EVENT_HANDLED
    
    def on_mouse_drag (self, x, y, dx, dy, button, modifiers):
        if not modifiers & pyglet.window.key.MOD_ALT: return
        if button==1:
            self.camera.x-=dx*2
            self.camera.y-=dy*2
        elif button==2:
            self.camera.x-=dx*2
            self.camera.z-=dy*2
        elif button==4:
            self.camera.ry+=dx/4.
            self.camera.rx-=dy/4.

class TuxImperium (object):
    def __init__ (self, window):
        self.window = window
        self.window.push_handlers(self.on_key_release)
        self.current_scene = None
        self.profiler = None
    
    def on_key_release (self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        elif symbol == pyglet.window.key.G:
            self.show_profiler()
            return pyglet.event.EVENT_HANDLED
        elif symbol == pyglet.window.key.S:
            pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot-%d.png' % (int(time.time())))
            return pyglet.event.EVENT_HANDLED
        elif symbol == pyglet.window.key.F:
            self.window.set_fullscreen(not self.window.fullscreen)
    
    def show_profiler (self):
        # FYI: Wont work if you don't have PyGTK
        if GPROFILER_ERROR:
            print 'Failed to initialize profiler (%s)' % GPROFILER_ERROR
            return
        if self.profiler:
            self.profiler.destroy()
        self.profiler = profiler.GProfiler()
        self.profiler.show()
            
    def scene_game (self):
        if self.current_scene:
            self.current_scene.end()
        self.current_scene = GameScene(self.window)

def main ():
    if LooseVersion(platform.python_version()) < LooseVersion('2.4'):
        print 'Warning: python version %s is unsupported.' % platform.python_version()
    if LooseVersion(pyglet.version) < LooseVersion('1.1.2') :
        print 'Warning: pyglet version %s is unsupported.' % pyglet.version
    if GPROFILER_ERROR:
        print 'Failed to initialize profiler (%s)' % GPROFILER_ERROR
    else:
        profiler.pyglet()
    game = TuxImperium(pyglet.window.Window(1000, 500))
    game.scene_game()
    pyglet.app.run()
    
if __name__ == '__main__':
    main()