points = []
def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5
def farthest_point(points):
    origin = (0, 0)
    farthest = points[0]

    for point in points:
        if distance(origin, point) > distance(origin, farthest):
            farthest = point

    return farthest
n = int(input("Enter number of points: "))
for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))
print("\nPoints:", points)
p1 = int(input("\nEnter first point number: "))
p2 = int(input("Enter second point number: "))
print("Distance:",
      distance(points[p1 - 1], points[p2 - 1]))
print("Farthest point from origin:", farthest_point(points))