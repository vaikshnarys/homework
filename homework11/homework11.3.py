import random
MY_LIST = ["s", "f", "q", "p", "s", "g"]
def name_generator(numbers):
    for number in range(1,numbers):
        name = "".join([random.choice(MY_LIST) for i in range(random.randint(1, 10))])
        yield name + str(number)
for item in name_generator(5):
    print(item)