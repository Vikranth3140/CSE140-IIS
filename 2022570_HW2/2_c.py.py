import math

# Define the end-effector position and link lengths
x = float(input('Enter the end effector value of x : '))
y = float(input('Enter the end effector value of y : '))
l1 = float(input('Enter the lenght L1 : '))
l2 = float(input('Enter the lenght L2 : '))

# Calculate theta2
cos_theta2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
theta2 = math.acos(cos_theta2)

# Calculate theta1
k1 = l1 + l2 * math.cos(theta2)
k2 = l2 * math.sin(theta2)
theta1 = math.atan2(y, x) - math.atan2(k2, k1)

# Print the joint angles (θ1, θ2) in radians
print('Joint angles (θ1, θ2) in radians:', theta1, theta2)