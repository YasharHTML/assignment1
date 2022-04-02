x_ = int(input("Enter the x part of the coordinate: ")) # getting the x part of the coordinate
y_ = int(input("Enter the y part of the coordinate: ")) # getting the y part of the coordinate
i = 0 # this determines if we are getting the second coordinate or not
pe = 0 # overall perimeter
x_pre = 0 # they are the "previous" values
y_pre = 0 # and this
def euclidean_distance(x, y): # this is the function to calculate the euclidean distance
    return ((x**2)+(y**2))**0.5 # this is the formula to calculate the euclidean distance

while True: # this is the loop to get the coordinates
    x = (input("Enter the x part of the coordinate (blank to quit): ")) # getting the x part of the coordinate
    if x == "": # if the x part of the coordinate is blank
        pe += euclidean_distance(x_ - x_pre, y_ - y_pre) # calculating the perimeter by calculating the end point to first input points
        break # we are breaking the loop
    y = (input("Enter the y part of the coordinate: ")) # getting the y part of the coordinate
    if i == 0: # if it is 2nd coordinate
        x = int(x) # we are converting the string to integer
        y = int(y) # we are converting the string to integer
        pe += euclidean_distance(x_ - x, y_ - y) # calculating the perimeter by calculating the 2 consecutive points
        i += 1 # we are increasing the amount of coordinates 
        x_pre = x # we are saving the x part of the coordinate
        y_pre = y # we are saving the y part of the coordinate
    else: # for every other coordinate 
        x = int(x) # we are converting the string to integer
        y = int(y) # we are converting the string to integer
        pe += euclidean_distance(x_pre - x, y_pre - y) # calculating the perimeter by calculating the 2 consecutive points
        x_pre = x # we are saving the x part of the coordinate
        y_pre = y # we are saving the y part of the coordinate
print("The perimeter of that polygon is {:.2f}".format(pe)) # printing the perimeter