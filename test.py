import hashlib
import uuid
import matplotlib.pyplot as plt
import time

EXP_NO = 101
VARIATION_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8]
VARIATION_LIST_SIZE = len(VARIATION_LIST)

def create_user():
    user_id = uuid.uuid4()
    with open("test.csv", "a+") as f:
        f.write(str(user_id) + ',')
    return user_id

def join_str(str1, str2):
    return (str(str1) + str(str2))

arr = []

start = time.perf_counter()
for i in range(10000):
    user = create_user()

    string = join_str(user, EXP_NO)

    m = hashlib.sha256()
    m.update(bytes(string, encoding="utf-8"))
    hash = m.hexdigest()
    arr.append(int(hash, 16) % VARIATION_LIST_SIZE)
print(time.perf_counter() - start)

count_arr = [arr.count(var) for var in VARIATION_LIST]

print("Count array - ", count_arr)

fig = plt.figure(figsize=(10, 7))
plt.pie(count_arr, labels=VARIATION_LIST)
plt.show()

