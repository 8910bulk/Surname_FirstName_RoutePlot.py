# This module converts route_file_out into a start point
# and then modifies the X and Y co-ordinates based on the movement

if __name__=="__main__":
    route = [1,1,"N"]
def create_route(route):
    currentx = int(route[0])
    currenty = int(route[1])
    xpoints = []
    ypoints = []
    xpoints.append(currentx)
    ypoints.append(currenty)

    for each in route[2:]:
        if each == "N":
            currenty += 1
        if each == "S":
            currenty -= 1
        if each == "W":
            currentx -= 1
        if each == "E":
            currentx += 1
        xpoints.append(currentx)
        ypoints.append(currenty)
    return (xpoints, ypoints)
