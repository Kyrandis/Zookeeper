HALF_LIFE = 0.5
N = int(input())  # number of atoms taken
R = int(input())  # the target number of atoms left over after half-life
T = 0  # the number of days it took to get to R

while N > R:
    N = N * HALF_LIFE
    T += 12
print(T)
