# We will be using sqrt (square root) and random (float number between 0 and 1) from math and random libraries.
import math
import random


# Calculate the theoretical expectation for Bernoulli trials
def successess(p, n):
    return n * p


# Calculate the theoretical standard deviation for Bernoulli trials using square root from math library.
def standardDeviation(p, n):
    return math.sqrt(n * p * (1 - p))


# Function that simulates Bernoulli trials with the help from random library.
def bernoulliTrials(p, n):
    return sum(random.random() < p for _ in range(n))


# Prompts user for input with error handling, ensuring p is between 0 and 1 to avoid confusion in code.
while True:
    try:
        p = float(input("Enter the probability. (Must be between zero and one): "))
        if 0 <= p <= 1:
            break
        else:
            print("Error: p must be between 0 and 1. Please try again.")
    except ValueError:
        print("Error: What are you writing here to get this even? (but here,take this 🥚)")


# Prompts user for input with error handling, ensuring n is a positive integer.
while True:
    try:
        n = int(input("Enter the number of trials: "))
        break
    except ValueError:
        print("Error: What are you writing here to get this even? (but here, take this 🥚)")


# Calculate and print theoretical values
expectation = successess(p, n)
standardDeviation = standardDeviation(p, n)
print(f"Theoretical Expectation: {expectation:.2f}")
print(f"Theoretical Standard Deviation: {standardDeviation:.2f}")


# Simulates 50, 100 and 1000 trials and prints the samples standard deviation.
for trials in [50, 100, 1000]:
    print(f"Simulating {trials} trials:")
    results = [bernoulliTrials(p, trials) for _ in range(1000)]
    print(f"Standard Deviation: {standardDeviation:.2f}")
