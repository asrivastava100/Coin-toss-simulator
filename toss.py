# The purpose of this program is to simulate coin tosses.

import random

toss = ["H", "T"]
no_of_tails = 0
no_of_tosses = 10000000

for i in range(no_of_tosses):
    observation = random.choice(toss)
    if observation == "T":
        no_of_tails += 1

print("No. of tails observed: " + str(no_of_tails))
print("No. of coin tosses: " + str(no_of_tosses))
print("Probability of tails is: " + str(no_of_tails / no_of_tosses))

'''
Sample run:

No. of tails observed: 49996091
No. of coin tosses: 100000000
Probability of tails is: 0.49996091
'''
