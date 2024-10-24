import math
# Data containing the dataset used for calculations.
sample_data = [2, 4, 4, 4, 5, 5, 7, 9]


# Calculate the mean of the data.
def meanData(data):
    return sum(data) / len(data)
# Calculate the variance of the data.
def varianceData(data):
    mean = meanData(data)
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    return squared_diff_sum / (len(data) - 1)  # Using n-1 for sample variance.


# Calculate the deviation of the data.
def deviationData(data):
    return math.sqrt(varianceData(data))


# Prints.
print(f"Sample Mean: {meanData(sample_data):.2f}")
print(f"Sample Variance: {varianceData(sample_data):.2f}")
print(f"Sample Standard Deviation: {deviationData(sample_data):.2f}")
# We use the function .2f to show two (2) decimals, but could increase this number to whichever fits the usecase.
