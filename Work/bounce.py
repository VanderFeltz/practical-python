# bounce.py
#
# Exercise 1.5

height = 100 # meters
bounce = 1

for bounce in range(1,11):
    height = height * 0.6
    print(bounce, round(height, 4))
    bounce += 1

