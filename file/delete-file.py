with open('text.txt') as fr:
    lines = fr.readlines()
    ptr =1
    with open('text.text','w') as fw:
        for lines in lines:
            if ptr!=5:
                fw.write(lines)
            ptr = ptr+1
        print("Deleted")