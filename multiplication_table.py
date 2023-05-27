# 乘法表
a = 1
while a < 10:
    c = 1
    while c <= a:
        print(f"{c}*{a}={a * c}", end="\t")
        c += 1
    print("")
    a += 1

print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end="\t")
    print()
