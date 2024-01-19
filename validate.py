import hashlib
import time

import logging
import coloredlogs

logger = logging.getLogger(__file__)
coloredlogs.install(level="DEBUG", logger=logger)

EXP_NO = 101
VARIATION_LIST = [0, 1, 2, 3]
VARIATION_LIST_SIZE = len(VARIATION_LIST)


def join_str(str1, str2):
    return str(str1) + str(str2)


arr = []
ids = []

start = time.perf_counter()
with open("test.csv", "r") as f:
    data = f.read()
    ids = data.split(",")
    ids.remove("")
print(time.perf_counter() - start)

start = time.perf_counter()
for id in ids:
    string = join_str(id, EXP_NO)

    m = hashlib.sha256()
    m.update(bytes(string, encoding="utf-8"))
    hash = m.hexdigest()
    arr.append(int(hash, 16) % VARIATION_LIST_SIZE)
print(time.perf_counter() - start)

count_arr = [arr.count(var) for var in VARIATION_LIST]

logger.info("Count array - %s", count_arr)
