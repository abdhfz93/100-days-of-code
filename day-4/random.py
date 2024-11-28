import random

random_integer = random.randint(1,2)
if random_integer == 2:
    print("head")
else:
    print("tail")

random_0_to_1 = random.random()
if random_0_to_1 >= 0.5:
    print("head")
else:
    print("tail")

random_float = random.uniform(0,1)
if random_float >= 0.5:
    print("head")
else:
    print("tail")