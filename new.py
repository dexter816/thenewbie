def main():
 import shelve
 s = shelve.open("drows.db")
 try:
     delrow(s, 'foo')
     delrow(s, 'bar')
     delrow(s, 0)

     s['0'] =  { 1:'foo',2:'bar',3:'lumberjack'}
     s["Hello"] =  { 1:'foo',2:'bar',3:'lumberjack'}
     s['Spam'] =  { 1:'foo',2:'bar',3:'lumberjack'}

              
                  
 finally:
   s.close()

 s = shelve.open("drows.db") 

 for item in s['0']:
     fname = (s['0'][item])
     if fname in globals():
         from inspect import signatureImportError: cannot import name signature


         sig = signature(eval(fname))
         print("%s is a function with arguments %s" % (fname,sig))
    
 for item in s:
     if item != '0':
      print(item + ": " + str(s[item]))

def delrow(s, rowkey):
  try:
      del s[rowkey]
  except:
         pass
def lumberjack(job, play='', status='OKay'):
    return"i,m Okay"


if __name__ == "__main__":
  main()


                                                                                                                                                                                
