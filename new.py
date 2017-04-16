import shelve
s = shelve.open("mydict.db")
try:
s["mydict"] = { 1:'foo',2:'bar',3:'lumberjack'}
finally:
    s.close()

    s = shelve.open("mydict.db")
    
    mydict = s["mydict"]

for item in mydict:
print(mydict[item])

                                                                                                                                                                                
