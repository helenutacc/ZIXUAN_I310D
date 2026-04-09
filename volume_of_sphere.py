import math

def calculate_volume_of_sphere(radius):
    # Volume of a sphere: V = (4/3) * pi * r^3
    return (4/3) * math.pi * radius ** 3

# Compute and print volumes for radii 30 and 40
for radius in [30, 40]:
    volume = calculate_volume_of_sphere(radius)
    print(f"Volume of sphere with radius {radius}: {volume:.2f}")
