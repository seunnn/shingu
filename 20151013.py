for i in range(10):
    if i==5:break
    print i
print "EOP"
for i in range(10):
    if i==5:continue
    print i
print "EOP"
i=0
while i<10:
    print i,
    i+=1
else:
    print "EOP"
