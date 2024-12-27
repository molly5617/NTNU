a = int(input())
score = 0
if a >= 0 and a <= 10:
    score = a * 6
elif a >= 11 and a <= 20:
    score = 10 * 6 + (a - 10) * 2
elif a >= 21 and a <= 40:
    score = 10 * 6 + 10 * 2 + (a - 20) * 1
else:
    score = 100
print(score)
