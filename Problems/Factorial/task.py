N = int(input())  # 3
factorial = 1
while 1 < N <= 100:
    factorial = factorial * N
    N = N - 1
print(factorial)

# 3! * 2 * 1 = 6
# 2! * 1 = 2
# 1! = 1
# 5 4 3 2 1
# 8 7 6 5 4 3 2 1