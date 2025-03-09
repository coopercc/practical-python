# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0
for i in range(10):
    height = height * 0.6
    bounce += 1
    print(bounce, round(height, 4))
