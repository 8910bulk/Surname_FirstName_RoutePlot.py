# import my functions
import read_route
import create_route
import matplotlib.pyplot as plot

xmax = 12
xmin = 1
ymax = 12
ymin = 1
validdirections = ("N","E","W","S")

#  while loop to keep trying files till user says STOP
route_file=""
while route_file !="stop":
    print("Enter the next route instructions file or enter STOP to finish:")
    route_file = str.lower(input())
    #check the file opens, if not don't try to evaluate the route
    try:
        open (route_file, 'r')
    except FileNotFoundError:
        print ("File not found.")
        continue
#process any file that opened
    else:
        route_file_out = read_route.read_route(route_file)
        # check for invalid directions
        route_file_directions = route_file_out[2::]
        directions_ok = bool
        legcount=1
        for each in route_file_directions:
            if each not in validdirections:
                print ("Error: Invalid direction on leg ", legcount)
                directions_ok = False
                legcount+=1
            else:
                legcount+=1

        xpoints, ypoints = create_route.create_route(route_file_out)

        #check if the route stays in the grid
        route_ok = bool
        too_far=""
        if int(max(xpoints)) > xmax:
            route_ok = False
            too_far = xpoints.index(xmax+1)
            route_error = "too far East"
        if int(min(xpoints)) < xmin:
            route_ok = False
            route_error = "too far West"
            too_far = xpoints.index(xmin-1)
        if int(max(ypoints)) > ymax:
            route_ok = False
            route_error = "too far North"
            too_far = ypoints.index(ymax+1)
        if int(min(ypoints)) < ymin:
            route_ok = False
            route_error = "too far South"
            too_far = ypoints.index(ymin-1)
        # print the error or make a graph
        if not route_ok:
            print("Error: The route goes outside of the grid - it goes", route_error, "on leg", too_far)
        elif route_ok and directions_ok:
            plot.plot(xpoints, ypoints)
            plot.show()
            print ("This route follows the following path: ")
            islice=0
            while islice < len(xpoints):
                print ("(", xpoints[islice], ",", ypoints[islice], ") to ", end="")
                islice+=1
            print("Enter the next route instructions file or enter STOP to finish:")
exit()