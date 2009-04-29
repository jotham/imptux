import imptux, pyglet, time, math
from pyglet import gl

class Terrain (object):
    model = pyglet.graphics.vertex_list(168,('v3f/static', (-400, 30, -2000, -330, 30, -2000, -330, 30, -2000, -330, 30, 0, -330, 30, 0, -400, 30, 0, -400, 30, 0, -400, 30, -2000, -330, 30, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, -2000, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -330, 30, 0, -330, 30, 0, -330, 30, -2000, -324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, -2000, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, 0, -324.956177, 29.579521, -2000, -319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, -2000, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, 0, -319.409271, 28.364159, -2000, -310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, -2000, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, 0, -310.095367, 25.20192, -2000, -283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, -2000, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, 0, -283.322876, 12.78336, -2000, -205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, -2000, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, 0, -205.223038, -23.061121, -2000, -160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, -2000, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, 0, -160.174072, -38.25024, -2000, -107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, -2000, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, 0, -107.280006, -50.640003, -2000, -56.760002, -57.48, -2000, 0, -60, -2000, 0, -60, -2000, 0, -60, 0, 0, -60, 0, -56.760002, -57.48, 0, -56.760002, -57.48, 0, -56.760002, -57.48, -2000, 0, -60, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, -2000, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 0, -60, 0, 0, -60, 0, 0, -60, -2000, 56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, -2000, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 56.400002, -57.48, 0, 56.400002, -57.48, 0, 56.400002, -57.48, -2000, 106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, -2000, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, 0, 106.000008, -50.640003, -2000, 149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, -2000, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, 0, 149.400009, -40.559998, -2000, 194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, -2000, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, 0, 194.140793, -25.70784, -2000, 248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, -2000, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 248.400009, -1.68, 0, 248.400009, -1.68, 0, 248.400009, -1.68, -2000, 302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, -2000, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, 0, 302.198395, 23.825281, -2000, 313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, -2000, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 313.200012, 27.48, 0, 313.200012, 27.48, 0, 313.200012, 27.48, -2000, 320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, -2000, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, 0, 320.126404, 29.066881, -2000, 323.481598, 29.579521, -2000, 330, 30, -2000, 330, 30, -2000, 330, 30, 0, 330, 30, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, 0, 323.481598, 29.579521, -2000, 330, 30, -2000, 400, 30, -2000, 400, 30, -2000, 400, 30, 0, 400, 30, 0, 330, 30, 0, 330, 30, 0, 330, 30, -2000)))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def update (self, dt):
        return True
    
    def draw (self):
        gl.glColor3f(0.38, 0, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()

class EnemyDrone (object):
    model = pyglet.graphics.vertex_list(32,('v3f/static', (-50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, -50.0, 10.000002, -100.0, 50.0, -9.999998, -100.0, 50.0, 10.000002, -100.0, 50.0, 10.000002, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, 50.0, -9.999998, -100.0, 50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, 50.0, 10.000002, -100.0, -50.0, 10.000002, -100.0, -50.0, -9.999998, -100.0, -50.0, -9.999998, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, -50.0, 10.000002, -100.0, -50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, 50.0, -9.999998, -100.0, 0.0, -2e-06, 0.0, 0.0, -2e-06, 0.0, -50.0, -9.999998, -100.0)))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.health = 10
        self.step = 0
        self.step_rate = math.pi/2
        
    def update (self, dt):
        self.step += self.step_rate * dt
        self.x = 200 * math.sin(self.step+self.z/200.0)
        return (self.health > 0)
    
    def draw (self):
        gl.glColor3f(1.0, 0, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
        
class PlayerBulletModel (object):
    model = pyglet.graphics.vertex_list(6, ('v3f/static', (-10, 0, 5, 0, 0, -5, 0, 0, -5, 10, 0, 5, 10, 0, 5, -10, 0, 5)))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vz = -500
        self.boundsz = -2000
        
    def draw (self):
        gl.glColor3f(1, 0.8, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
    
    def update (self, dt):
        self.z += self.vz * dt
        return (self.z > self.boundsz)

class Player (object):
    model = pyglet.graphics.vertex_list(32,('v3f/static', (-50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, -50.0, 10.000002, 0.0, 50.0, -9.999998, 0.0, 50.0, 10.000002, 0.0, 50.0, 10.000002, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, 50.0, -9.999998, 0.0, 50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, 50.0, 10.000002, 0.0, -50.0, 10.000002, 0.0, -50.0, -9.999998, 0.0, -50.0, -9.999998, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, -50.0, 10.000002, 0.0, -50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, 50.0, -9.999998, 0.0, 0.0, -2e-06, -100.0, 0.0, -2e-06, -100.0, -50.0, -9.999998, 0.0)))
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.decay = 1
        self.iv = 350
        self.fire_delay = .25
        self.timestamp = 0
        self.boundsx = 200
        
    def draw (self):
        gl.glColor3f(0, 0.8, 0)
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, self.z)
        self.model.draw(gl.GL_LINES)
        gl.glPopMatrix()
    
    def update (self, dt):
        self.x = max(-self.boundsx, min(self.boundsx, self.x + (self.vx * dt) ))
        self.vx *= self.decay
        return True
        
    def move_left (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = -self.iv
        elif self.vx < 0:
            self.decay = 0.9
            
    def move_right (self, mode):
        if mode == 1:
            self.decay = 1
            self.vx = self.iv
        elif self.vx > 0:
            self.decay = 0.9
        
    def fire (self, now):
        if now > self.timestamp:
            self.timestamp = now + self.fire_delay
            return (PlayerBulletModel(self.x-40, self.y, self.z-18), PlayerBulletModel(self.x+40, self.y, self.z-18))
        return None

class GameScene (object):
    def __init__ (self, window, framerate=60.0):
        self.window = window
        self.width = window.width
        self.height = window.height
        self.window.push_handlers(self)
        self.camera = imptux.Camera()
        pyglet.clock.schedule_interval(self.update_game, 1/framerate) 
        self.clock = pyglet.clock.ClockDisplay()
        self.new_game()
        
    def new_game (self):
        self.entities = []
        self.terrain = Terrain(0, -200, 0)
        self.entities.append(self.terrain)
        self.player = Player(0, -200, 0)
        self.entities.append(self.player)
        for n in xrange(14):
            self.entities.append(EnemyDrone(n*-100, -100, -300 + n*-110))
        
    def update_game (self, dt):
        temp = []
        for entity in self.entities:
            if entity.update(dt):
                temp.append(entity)
        self.entities = temp
        self.camera.update()
        self.window.invalid = True
        
    def end (self):
        pyglet.clock.unschedule(self.update)
        self.window.pop_handlers()
    
    def on_draw (self):
        self.window.clear()
        self.camera.position()
        for entity in self.entities:
            entity.draw()
        self.border.draw()
        gl.glEnable(gl.GL_DEPTH_TEST)
        self.axis.draw()
        gl.glDisable(gl.GL_DEPTH_TEST)
        gl.glTranslatef(self.width/2-160, self.height/-2+20, 0)
        self.clock.draw()
        self.window.invalid = False
        
    def on_key_press (self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        if symbol == pyglet.window.key.A:
            self.player.move_left(1)
        elif symbol == pyglet.window.key.D:
            self.player.move_right(1)
        
    def on_key_release (self, symbol, modifiers):
        if symbol == pyglet.window.key.A:
            self.player.move_left(0)
        elif symbol == pyglet.window.key.D:
            self.player.move_right(0)
        
    def on_mouse_press (self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            munitions = self.player.fire(time.time())
            if munitions:
                self.entities.extend(munitions)
    
    def on_resize (self, width, height):
        self.width = width
        self.height = height
        self.camera.defaultView(width, height)
        self.border = imptux.Border(self.width-32, self.height-32)
        self.axis = imptux.Axis(40+self.width/-2, 40+self.height/-2, 0)
        self.window.invalid = True
        return pyglet.event.EVENT_HANDLED
    
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
            
class TuxImperium (object):
    def __init__ (self, window):
        self.window = window
        self.current_scene = None
        
    def scene_game(self):
        if self.current_scene:
            self.current_scene.end()
        self.current_scene = GameScene(self.window)

def main ():
    game = TuxImperium(pyglet.window.Window(900, 555))
    game.scene_game()
    pyglet.app.run()
    
if __name__ == '__main__':
    main()