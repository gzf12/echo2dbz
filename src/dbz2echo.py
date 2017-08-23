bits = []
height = 400
width = 400
data = []

for x in xrange(height):
    for y in xrange(width):
        index = x * width + y
        bits[index] = int(data[index]) * 2 + 20