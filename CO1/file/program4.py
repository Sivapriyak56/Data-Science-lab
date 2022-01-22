firstfile = input("Enter a file name")
secondfile = input("Enter second file name")

f1=open(firstfile,"r")
f2=open(secondfile,"r")

print("before appending first file --",f1.read())
print("before appending second file --",f2.read())
f1.close()
f2.close()

f1 = open(firstfile,'a+')
f2 = open(secondfile,'r')

f1.write(f2.read())

print("after appending first file--",f1.read())
print("after appending second file--",f2.read())
f1.close()
f2.close()
