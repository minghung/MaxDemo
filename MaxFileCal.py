# -*- coding: utf-8 -*-
class calc:
    """
    用途：針對將鍵盤輸入的數字，
    提供下列功能
        input():放入指定的檔案
        print():列出檔案內的數字
        add():計算出檔案中的數字相加的結果
        product():計算出檔案中的數字相乘的結果     
    """
    def __init__(self,filename):
        self.filename=filename
        self.buffer=[]
        
    def input(self):
        "將鍵盤輸入的數字放進檔案中"
        with open(self.filename,"w") as f:
            while True:
                s=input("enter a number(EXIT to terminate)?")
                if s.upper()=="EXIT":
                   break;
                   
                try:
                    f.write(int(s)+"\n")
                except ValueError:        
                    print(s,r" isn't number ,input again please") 

    def _load(self):
        "將檔案內的數字讀出來"
        with open(self.filename) as f:
            for line in f:
                self.buffer.append(int(line))
    
    def print(self):   
        "印出檔案內的數字" 
        print (self.buffer)
        if self.buffer == []:
            self._load()
        
        for an in self.buffer:
            print("the file has " ,an,endof='')

    def add(self):
        "計算出檔案中的數字相加的結果"
        if self.buffer == []:
            self._load()

        s = sum(self.buffer)
        print("add is",s) 

    def product(self):
        "計算出檔案中的數字相乘的結果"
        if self.buffer == []:
            self._load()        

        p = 1
        for n in self.buffer:
            p *= n
        print("product is ",p)        




def main():    
    
    fn=input("enter a filename?")   #輸入數字存放的檔名
    c=calc(fn)
    c.input()                       #將輸入的數字寫入檔案
    c.print()                       #印出檔案內的數字
    c.add()                         #將檔案內的數字相加
    c.product()                     #將檔案內的數字相乘
    

if __name__ == "__main__":
    main()




             