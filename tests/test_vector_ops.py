from src.vector import Vector

v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
addition = v + w
print('addition: {}'.format(addition))

v = Vector([7.119, 8.215])
w = Vector([-8.223, 0.878])
subtraction = v - w
print('subtraction: {}'.format(subtraction))

v = Vector([1.671, -1.012, -0.318])
multiplication = v.scalar_product(7.41)
print('multiplication: {}'.format(multiplication))

# *****************

v = Vector([-0.221, 7.437])
first_magnitude = v.magnitude()
print('first_magnitude: {}'.format(round(first_magnitude, 3)))

v = Vector([8.813, -1.331, -6.247])
second_magnitude = v.magnitude()
print('second_magnitude: {}'.format(round(second_magnitude, 3)))

v = Vector([5.581, -2.136])
first_normalization = v.normalize()
print('first_normalization: {}'.format(first_normalization))

v = Vector([1.996, 3.108, -4.554])
second_normalization = v.normalize()
print('second_normalization: {}'.format(second_normalization))

# *****************

v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
dot_product = v.dot_product(w)
print('first_dot_product: {}'.format(round(dot_product, 3)))

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
dot_product = v.dot_product(w)
print('second_dot_product: {}'.format(round(dot_product, 3)))

# *****************

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
angle_rads = v.get_angle_rad(w)
print('first_angle_rads: {}'.format(angle_rads))

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
angle_degrees = v.get_angle_deg(w)
print('first_angle_rads: {}'.format(angle_degrees))

# *****************

v = Vector([-7.579, -8.88])
w = Vector([22.737, 23.64])
is_parallel = v.is_parallel_to(w)
is_orthogonal = v.is_orthogonal_to(w)

print('1 parallel: {}, orthogonal: {}'.format(is_parallel, is_orthogonal))

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
is_parallel = v.is_parallel_to(w)
is_orthogonal = v.is_orthogonal_to(w)

print('2 parallel: {}, orthogonal: {}'.format(is_parallel, is_orthogonal))

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
is_parallel = v.is_parallel_to(w)
is_orthogonal = v.is_orthogonal_to(w)
print('3 parallel: {}, orthogonal: {}'.format(is_parallel, is_orthogonal))

v = Vector([2.118, 4.827])
w = Vector([0, 0])
is_parallel = v.is_parallel_to(w)
is_orthogonal = v.is_orthogonal_to(w)

print('4 parallel: {}, orthogonal: {}'.format(is_parallel, is_orthogonal))

# *****************

v = Vector([3.039, 1.879])
w = Vector([0.825, 2.036])
projected_vector = v.component_parallel_to(w)

print('projected vector is: {}'.format(projected_vector))

v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])
orthogonal_vector = v.component_orthogonal_to(w)

print('orthogonal vector is: {}'.format(orthogonal_vector))

v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])
projected_vector = v.component_parallel_to(w)
orthogonal_vector = v.component_orthogonal_to(w)

print('second projected vector is: {}'.format(projected_vector))

print('second orthogonal vector is: {}'.format(orthogonal_vector))

# *****************

v1 = Vector([8.462, 7.893, -8.187])
w1 = Vector([6.984, -5.975, 4.778])

v2 = Vector([-8.987, -9.838, 5.031])
w2 = Vector([-4.268, -1.861, -8.866])

v3 = Vector([1.5, 9.547, 3.691])
w3 = Vector([-6.007, 0.124, 5.772])

first_cross_product = v1.cross_product(w1)
print('cross product is: {}'.format(first_cross_product))

area_parallelogram = v2.area_of_parallelogram_with(w2)
print('area parallelogram is: {}'.format(round(area_parallelogram, 3)))

area_triangle = v3.area_of_triangle_with(w3)
print('area triangle is: {}'.format(round(area_triangle, 3)))