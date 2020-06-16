# put your python code here
individual = int(input())
hundreds = individual // 100
tens = individual // 10 % 10
ones = individual % 10
print(hundreds + tens + ones)
