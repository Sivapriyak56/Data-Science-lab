with open("text.txt") as f:
    with open("text2.txt","w") as f1:
        for line in f:
            f1.write(line)