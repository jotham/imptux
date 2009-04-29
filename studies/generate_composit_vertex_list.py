def main (filename, ox=0, oy=0, oz=0, sx=1, sy=1, sz=1):
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
                vertex_list.extend([ox+sx*float(last[0]), oy+sy*float(last[1]), oz+sz*float(last[2]), ox+sx*float(verticies[i][0]), oy+sy*float(verticies[i][1]), oz+sz*float(verticies[i][2])])
            else:
                first = (verticies[i][0], verticies[i][1], verticies[i][2])
            last = (verticies[i][0], verticies[i][1], verticies[i][2])
        vertex_list.extend([ox+sx*float(last[0]), oy+sy*float(last[1]), oz+sz*float(last[2]), ox+sx*float(first[0]), oy+sy*float(first[1]), oz+sz*float(first[2])])
        output_lists.extend(vertex_list)
    
    #~ for vertex_list in output_lists:
    count = len(output_lists)/3
        #~ print "pyglet.graphics.vertex_list(%d,('v3f/static', %s), ('c3B/static', %s))" % (count, '('+(', '.join(vertex_list))+')', (255,255,255)*count)
    print "pyglet.graphics.vertex_list(%d,('v3f/static', %s))" % (count, '('+(', '.join([str(n) for n in output_lists]))+')')
    objfile.close()
    
if __name__ == '__main__':
    main('drone.obj', 0, 0, -50, 0.5, 0.5, -0.5)