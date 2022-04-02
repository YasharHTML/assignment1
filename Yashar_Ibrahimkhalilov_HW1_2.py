x_ = int(input("Enter the x part of the coordinate: "))
y_ = int(input("Enter the y part of the coordinate: "))
i = 0
pe = 0
x_pre = 0
y_pre = 0
def euclidean_distance(x, y):
    return ((x**2)+(y**2))**0.5

while True:
    x = (input("Enter the x part of the coordinate (blank to quit): "))
    if x == "":
        pe += euclidean_distance(x_ - x_pre, y_ - y_pre)
        break
    y = (input("Enter the y part of the coordinate: "))
    if i == 0:
        x = int(x)
        y = int(y)
        pe += euclidean_distance(x_ - x, y_ - y)
        i += 1
        x_pre = x
        y_pre = y
    else:
        x = int(x)
        y = int(y)
        pe += euclidean_distance(x_pre - x, y_pre - y)
        i += 1
        x_pre = x
        y_pre = y
print("The perimeter of that polygon is {:.2f}".format(pe))