import sys
import pickle

def showmember(team):
    '''將dict的內容顯示出來'''
    if team==[]:
        print("來自檔案")
        team=loadmember()
        print(team)
    else:
        print("the team member is ")
        print("--------------")
        for member in team :
            print(member)
            #print(member[0],member[1])
        print("--------------")

def loadmember():
    '''將資料由檔案取出放進dict'''
    filename = input("Enter filename to open? ")

    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except:
        print(r"存檔失敗!!")


def savemember(team):
    '''將dict的資料放進檔案內'''
    print(team)
    filename = input("Enter filename to save? ")
    
    with open(filename, "wb") as f:
        pickle.dump(team, f)
    
    del team

def addmember(team):
    '''將資料放進dict'''
    newmember={}
    id = int(input("New Employee Id? "))
    name = input("New Employee Name? ")
    newmember[id]=name
    team.append(newmember)

def deletemember():
    '''刪掉dict內的資料'''
    #print ("delete member...")

def searchmember():
    '''找出dict內符合的資料'''
    #print ("search member...")

def takeaway():
    pass
    #sys.exit()


def main():
    '''初始'''
    #team=[{1:"max"},{2:"nana"}]
    team=[]
    '''顯示選單'''
    while True:
        print ()
        print ("1.show member")
        print ("2.save team member")
        print ("3.add member")
        print ("4.delete member")
        print ("5.search member")
        print ("0.exit")
        try:
            an=int(input("please enter a number of action(0~9):"))
        except:
            print(an," not a number,seclect again!!")
    

        if an==1:
            showmember(team)
        elif an==2:
            savemember(team)
        elif an==3:
            addmember(team)
        elif an==4:
            deletemember()
        elif an==5:
            searchmember()
        else:
            takeaway()
            
if __name__=="__main__":
    main()