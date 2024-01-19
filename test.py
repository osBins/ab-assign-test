import hashlib
import uuid
import matplotlib.pyplot as plt

EXP_NO = 101
def create_user():
    user_id = uuid.uuid4()
    with open("test.csv", "a") as f:
        f.write(str(user_id) + ',')
    return user_id

def join_str(str1, str2):
    return (str(str1) + str(str2))

arr = []

for i in range(1000):
    user = create_user()

    string = join_str(user, EXP_NO)

    m = hashlib.sha256()
    m.update(bytes(string, encoding="utf-8"))
    hash = m.hexdigest()
    arr.append(int(hash, 16) % 3)

count = [arr.count(0), arr.count(1), arr.count(2)]
print(count)
digits = [0, 1, 2]
fig = plt.figure(figsize=(10, 7))
plt.pie(count, labels=digits)

plt.show()

# [330, 348, 322]


