import hashlib

EXP_NO = 101

def join_str(str1, str2):
    return (str(str1) + str(str2))

arr = []
ids = []
with open("test.csv", "r") as f:
    data = f.read()
    ids = data.split(',')
    
for id in ids:
    string = join_str(id, EXP_NO)
    
    m = hashlib.sha256()
    m.update(bytes(string, encoding="utf-8"))
    hash = m.hexdigest()
    arr.append(int(hash, 16) % 3)

count = [arr.count(0), arr.count(1), arr.count(2)]
print(count) 
    