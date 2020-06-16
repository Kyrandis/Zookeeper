# put your python code here
days_stay = int(input())
food_cost = int(input())
flight1 = int(input())
hotel_cost = int(input())

cash = (food_cost * days_stay) + (hotel_cost * (days_stay - 1)) + (flight1 * 2)
print(cash)