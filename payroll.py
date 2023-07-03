money = 10000

for i in range(1, 21):
    if i > 1:
        input("再发一位?")

    if money >= 1000:
        import random

        score = random.randint(1, 10)

        if score < 5:
            print(f"员工{i}绩效为{score}，绩效太低不发工资，下一位")
            print(f"账户还剩{money}元\n")
            continue
        else:
            print(f"员工{i}绩效为{score}，发工资")
            money -= 1000
            print(f"账户还剩{money}元\n")
    else:
        print("没钱了")
        break