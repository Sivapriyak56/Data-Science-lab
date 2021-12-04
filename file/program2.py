file = open('text.txt','r')
count =0
content=file.read()
colist = content.split("\n")
for i in colist:
    if i:
        count = count+1
print("No.of line :" ,count)