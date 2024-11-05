import random
import math
import statistics

# Create the initial variables
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# Experimenting with a subset of integers 1-100
sum_sample = sum(vals_sample)
average_sample = statistics.mean(vals_sample)
median_sample = statistics.median(vals_sample)

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sum_sample}")
print(f"Average of 75 sample values: {average_sample}")
print(f"Median of 75 sample values: {median_sample}")
print('\n')

# Experimenting with a superset of 200 values, integers 1-100
average_choices = statistics.mean(vals_choices)
median_choices = statistics.median(vals_choices)
mode_choices = statistics.mode(vals_choices)
stdev_choices = statistics.stdev(vals_choices)
variance_choices = statistics.variance(vals_choices)

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {average_choices}")
print(f"Median of 200 values: {median_choices}")
print(f"Mode of 200 values: {mode_choices}")
print(f"Standard deviation of 200 values: {stdev_choices}")
print(f"Variance of 200 values: {variance_choices}")
print('\n')

# Modeling a random circle
area = pi * (radius ** 2)
area_rounded_up = math.ceil(area)
area_rounded_down = math.floor(area)

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_rounded_down} (rounded down to the nearest integer)")
