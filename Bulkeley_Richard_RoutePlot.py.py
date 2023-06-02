# import my functions
import read_route
import create_route
import matplotlib.pyplot as plot

# infinite while loop to keep trying files till user says STOP
while True:
    print("Enter the next route instructions file or enter STOP to finish:")
    route_file = str.lower(input())
    if route_file == "stop": break
#check the file opens, if not don't try to evaluate the route
    try:
        open (route_file, 'r')
    except FileNotFoundError:
        print ("File not found.")
        continue
#process any file that opened
    else:
        route_file_out = read_route.read_route(route_file)
        xpoints, ypoints = create_route.create_route(route_file_out)
        #check if the route stays in the grid
        route_ok = bool
        too_far=""
        if int(max(xpoints)) > 12:
            route_ok = False
            too_far = xpoints.index(13)
            route_error = "too far East"
        if int(min(xpoints)) < 1:
            route_ok = False
            route_error = "too far West"
            too_far = xpoints.index(0)
        if int(max(ypoints)) > 12:
            route_ok = False
            route_error = "too far North"
            too_far = ypoints.index(13)
        if int(min(ypoints)) < 1:
            route_ok = False
            route_error = "too far South"
            too_far = ypoints.index(0)
        # print the error or make a graph
        if not route_ok:
            print("Error: The route goes outside of the grid - it goes", route_error, "on leg", too_far)
        elif route_ok:
            plot.plot(xpoints, ypoints)
            plot.show()
            print ("This route goes from: ", xpoints[0], ",", ypoints[0], " to ", xpoints[-1], ",", ypoints[-1], sep="")
exit()
