import sys
import pickle

def membersearch(team,tgid=None,tgname=None):
    print(team)
    result="比對不到符合的資料"
    if tgid != None:
        for id,name in team.items():
            if tgname == id:
                result= id,"-",name
    elif tgname != None:
        for id,name in team.items():
            if tgname == name:
                result= id,"-",name
    return result

def showmember(team):
    '''將dict的內容顯示出來'''
    if team == None:
        return
    print("the team member is ")
    print("--------------")
    for id,name in team.items() :
        print(id,"-",name)
    print("--------------")

def __loadmember():
    '''將資料由檔案取出放進dict'''
    filename = input("Enter filename to open? ")

    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except TypeError:
        print(r"讀檔失敗!!")
    except FileNotFoundError:
        print(r"檔案不存在!!")
        
def savemember(team):
    '''將dict的資料放進檔案內'''
    filename = input(r"Enter filename to save? ")
    
    with open(filename, "wb") as f:
        pickle.dump(team, f)
    
    del team

def addmember(team):
    '''將資料放進dict'''
    id = input("New Employee Id? ")
    name = input("New Employee Name? ")
    print(team)
    result=membersearch(team=team,tgname=name)
    print(result)
    if "-" in result:
        result=name+"已存在"
        print(result)
    else:
        team[id]=name
        result=name+"新增完成"
        print(result)

def deletemember(team):
    '''刪掉dict內的資料'''
    tgname = input("Enter the name of member? ")
    result=membersearch(team=team,tgname=tgname)
    if "-" in result:
        del team[id]
        result=tgname+"已刪除"
        print(result)
    else:
        result=tgname+"不是member"
        print(result)

def searchmember(team):
    '''找出dict內符合的資料'''
    item=input("input id or name?")
    if item=="id":
        tgid=input("input id:")
        result=membersearch(team=team,tgid=tgid)
    else:
        tgname=input("input name:")
        result=membersearch(team=team,tgname=tgname)
    
    print("查詢的結果為",result)

def takeaway():
    pass
    #sys.exit()


def main():
    '''初始'''
    #team={"1":"max","2":"nana"}
    team={}
    '''顯示選單'''
    while True:
        print ("input below number that you want to do:")
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
            if team=={}:
                print("將由檔案取出team member的清單!")
                team=__loadmember()

            showmember(team)
        
        elif an==2:
            savemember(team)
        
        elif an==3:
            if team=={}:
                team=__loadmember()
            addmember(team)
        
        elif an==4:
            if team=={}:
                team=__loadmember()
            
            deletemember(team)

        elif an==5:
            if team=={}:
                team=__loadmember()
            searchmember(team)
        
        else:
            takeaway()
            
if __name__=="__main__":
    main()