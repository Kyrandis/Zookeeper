# put your python code here
length = int(input())
width = int(input())
height = int(input())

sum_edge = 4 * (length + width + height)
surf_area = 2 * (length * width + width * height + length * height)
volume = length * width * height

print(sum_edge)
print(surf_area)
print(volume)
