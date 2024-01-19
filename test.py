import hashlib
import uuid
import matplotlib.pyplot as plt
import time

import logging
import coloredlogs

logger = logging.getLogger("test.py")
coloredlogs.install(level="DEBUG", logger=logger)

EXP_NO = 101
ITERATIONS = 10000
VARIATION_LIST = [0, 1, 2, 3]
VARIATION_LIST_SIZE = len(VARIATION_LIST)


def create_user():
    user_id = uuid.uuid4()
    with open("test.csv", "a+") as f:
        f.write(str(user_id) + ",")
    return user_id


def join_str(str1, str2):
    return str(str1) + str(str2)


def get_time_taken(start_time):
    return time.perf_counter() - start_time


def create_hash(string):
    m = hashlib.sha256()
    m.update(bytes(string, encoding="utf-8"))
    return m.hexdigest()


def assign_variations(ITERATIONS, arr):
    for i in range(ITERATIONS):
        user = create_user()

        string = join_str(user, EXP_NO)

        hash = create_hash(string)

        arr.append(int(hash, 16) % VARIATION_LIST_SIZE)


def show_plot(arr):
    fig = plt.figure(figsize=(10, 7))
    plt.pie(arr, labels=VARIATION_LIST)
    plt.show()


def main():
    arr = []

    start_time = time.perf_counter()
    assign_variations(ITERATIONS, arr)
    print(get_time_taken(start_time))

    count_arr = [arr.count(var) for var in VARIATION_LIST]

    logger.info("Count array - %s", count_arr)

    show_plot(count_arr)


if __name__ == "__main__":
    main()
