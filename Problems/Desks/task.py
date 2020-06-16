# put your python code here

# students in each class
group1, group2, group3 = abs(int(input())), abs(int(input())), abs(int(input()))

# desks to purchase
room1 = group1 % 2 + group1 // 2
room2 = group2 % 2 + group2 // 2
room3 = group3 % 2 + group3 // 2
desks = room1 + room2 + room3
print(desks)
