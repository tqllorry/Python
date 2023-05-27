with open("/Users/tangqiliang/Desktop/bb.txt", "w") as copy:
    with open("/Users/tangqiliang/Desktop/aa.txt") as f:
        for a in f:
            if a.split(",")[-1].strip() == "test":
                continue
            copy.write(a)