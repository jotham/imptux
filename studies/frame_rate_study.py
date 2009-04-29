import pyglet
from pyglet import gl

def main ():
    width = 512
    height = 384
    window = pyglet.window.Window(width, height)
    size = 256
    vertex_list = pyglet.graphics.vertex_list(6,
        ('v3f/static', (0,0,0,size,0,0,0,0,0,0,size,0,0,0,0,0,0,size)), 
        ('c3B/static', (255,0,0,255,0,0,0,255,0,0,255,0,0,0,255,0,0,255)))
    rotation = [0,0,0]
    
    def on_resize(width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.gluPerspective(60, width/float(height), .1, 8192.)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        return pyglet.event.EVENT_HANDLED
    
    def on_draw ():
        window.clear()
        gl.glLoadIdentity()
        gl.glTranslatef(0, -128, -512)
        gl.glRotatef(rotation[1],0,1,0)
        vertex_list.draw(gl.GL_LINES)
        window.invalid = False
        
    def update (dt):
        rotation[1] += 90*dt
        window.invalid = True
        
    window.push_handlers(on_draw, on_resize)
    pyglet.clock.schedule_interval(update, 1/30.)
    pyglet.app.run()
    
if __name__ == '__main__':
    main()