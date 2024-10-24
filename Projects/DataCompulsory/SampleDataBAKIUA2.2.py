import random


# Function that returns one and zero based on outcomes instead of true and false.
def bernoulliTrial(p):
    return 1 if random.random() < p else 0




# Function to calculate total successes in n trials.
def successes(n, p):
    return sum(bernoulliTrial(p) for _ in range(n))


'''
With the hypothetical scenario of a coinflip.
I used the bernoulli trial to simulate a coinflip 100 times.
Assuming it will always end up on one side and not in the middle.
'''
trials = 100
successRateData = 0.5
successesData = successes(trials, successRateData)
print(f"Total successes in {trials} trials with probability of {successRateData} is")
print(successesData)


# Example of generating individual outcomes
print("Individual trials with the probability of 50%:")
for _ in range(10):
    print(bernoulliTrial(successRateData), end=" ")
