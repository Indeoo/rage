import time
from tqdm import tqdm
import random


def randomized_sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)


def int_to_decimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))
