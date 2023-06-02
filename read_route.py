def read_route(route_file):
    output=[]
    current_route = open (route_file, 'r')
    count=0
    while True:
            count  += 1
            line = current_route.readline()
            if not line:
                    break
            else: output.append(line.strip('\n'))
    current_route.close()
    return (output)
