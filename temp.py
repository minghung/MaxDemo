# -*- coding: utf-8 -*-
class calc:
    def __init__(self,filename):
        self.filename=filename
        self.buffer=[]
        
            
    def load(self):
        with open(self.filename) as f:
            for line in f:
                self.buffer.append(int(line))
    
    def print(self):    
        if self.buffer == None:
            self.load()
        
        for an in self.buffer:
            print(an)
        
    def add(self):
        s = sum(self.buffer)
        print(s) 

    def product(self):
        p = 1
        for n in self.buffer:
            p *= n
        print(p)        


fn=input("enter a filename?")
print(fn)


with open(fn,"w") as f:

    while True:
        s=input("enter a number(EXIT to terminate)?")
        if s.upper()=="EXIT":
            break;
        f.write(s+"\n")  


        

c=calc(fn)
c.load()
c.add()
c.product()
c.print()


             