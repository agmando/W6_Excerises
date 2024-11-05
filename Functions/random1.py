import random

fruits = ["apple", "banana", "cherry", "peach", "plum", "watermelon"]

chosen_fruit = random.choice(fruits)
print(f"Random choice from fruits: {chosen_fruit}")

random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

random_uniform = random.uniform(5.5, 10.5)
print(f"Random float between 5.5 and 10.5: {random_uniform}")

random.shuffle(fruits)
print(f"Shuffled fruits list: {fruits}")

sampled_fruits = random.sample(fruits, 3)
print(f"Random sample of 3 fruits: {sampled_fruits}")

weighted_choices = random.choices(fruits, weights=[1, 2, 1, 2, 1, 3], k=4)
print(f"Random choices with weights: {weighted_choices}")

print("\nExperimenting with repeated calls:")


print(f"Random choice: {random.choice(fruits)}")
print(f"Random choice: {random.choice(fruits)}")
print(f"Random choice: {random.choice(fruits)}")

print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random integer (1-10): {random.randint(1, 10)}")

print(f"Random float (0.0-1.0): {random.random()}")
print(f"Random float (0.0-1.0): {random.random()}")
print(f"Random float (0.0-1.0): {random.random()}")


print(f"Random sample of 2 fruits: {random.sample(fruits, 2)}")
print(f"Random sample of 2 fruits: {random.sample(fruits, 2)}")
print(f"Random sample of 2 fruits: {random.sample(fruits, 2)}")