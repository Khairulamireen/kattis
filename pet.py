winner = 0
score = 0
num_of_contestant = 3

for i in range (1, num_of_contestant+1):
    point = [int(x) for x in input().split()]
    contestant_score = sum(point)
    if contestant_score > score:
        winner = i
        score = contestant_score

print(winner, score)