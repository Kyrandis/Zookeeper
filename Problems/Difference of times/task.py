# put your python code here
hours1 = int(input())
minutes1 = int(input())
result1 = int(input())

hours2 = int(input())
minutes2 = int(input())
result2 = int(input())

time1 = (hours1 * 3600) + (minutes1 * 60) + result1
time2 = (hours2 * 3600) + (minutes2 * 60) + result2

# output is in seconds
final = time2 - time1
print(final)
