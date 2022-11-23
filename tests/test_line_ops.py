from src.line import Line
from src.vector import Vector

# first system
# 4.046x + 2.836y = 1.21
# 10.115x + 7.09y = 3.025

line1 = Line(Vector([4.046, 2.836]), 1.21)
line2 = Line(Vector([10.115, 7.09]), 3.025)

print('first system intersect in: {}'.format(line1.intersection(line2)))

# second system
# 7.204x + 3.182y = 8.68
# 8.172x + 4.114y = 9.883

line3 = Line(Vector([7.204, 3.182]), 8.68)
line4 = Line(Vector([8.172, 4.114]), 9.883)

print('second system intersect in: {}'.format(line3.intersection(line4)))

# third system
# 1.182x + 5.562y = 6.744
# 1.773x + 8.343y = 9.525

line5 = Line(Vector([1.182, 5.562]), 6.744)
line6 = Line(Vector([1.773, 8.343]), 9.525)

print('third system intersect in: {}'.format(line5.intersection(line6)))
