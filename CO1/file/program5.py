import filecmp

f = "C:\Users\user\PycharmProjects\pythonProject1/text.txt"
f1 = "C:\Users\user\PycharmProjects\pythonProject1/text2.txt"

result = filecmp.cmp(f,f1)
print(result)