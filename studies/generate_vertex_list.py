def main (filename):
    objfile = file(filename, 'r')
    verticies = []
    faces = []
    for line in objfile.readlines():
        parts = line.strip().split(' ')
        if len(parts) == 1:
            continue
        if parts[0] == 'v':
            verticies.append(parts[1:])
        elif parts[0] == 'f':
            faces.append(parts[1:])
    output_lists = []
    for face in faces:
        first = last = None
        vertex_list = []
        for part in face:
            elements = part.split('/')
            i = int(elements[0])-1
            if last:
                vertex_list.extend([last[0], last[1], last[2], verticies[i][0], verticies[i][1], verticies[i][2]])
            else:
                first = (verticies[i][0], verticies[i][1], verticies[i][2])
            last = (verticies[i][0], verticies[i][1], verticies[i][2])
        vertex_list.extend([last[0], last[1], last[2], first[0], first[1], first[2]])
        output_lists.append(vertex_list)
    
    for vertex_list in output_lists:
        count = len(vertex_list)/3
        #~ print "pyglet.graphics.vertex_list(%d,('v3f/static', %s), ('c3B/static', %s))" % (count, '('+(', '.join(vertex_list))+')', (255,255,255)*count)
        print "pyglet.graphics.vertex_list(%d,('v3f/static', %s))," % (count, '('+(', '.join(vertex_list))+')')
    objfile.close()
    
if __name__ == '__main__':
    main('cage.obj')