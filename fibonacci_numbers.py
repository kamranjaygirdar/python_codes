
print(0)
first=0
second=1
last=first+second
print("{0}\n{1}".format(second,last))

i=1

for i in range(6):
    
    first=second
    second=last
    last=first+second
    print(last)
    


