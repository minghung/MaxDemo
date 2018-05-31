import sys
import pickle
import json

def __membersearch(team,tgid=None,tgname=None):
    result="比對不到符合的資料"
    if team=={}:
        pass
    else:
        if tgid != None:
            for id,name in team.items():
                if tgid == id:
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

def __loadmemberfrompickle():
    '''將資料由檔案取出放進dict'''
    filename = input("Enter filename to open? ")

    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except TypeError:
        print(r"讀檔失敗!!")
        return {}
    except FileNotFoundError:
        print(r"檔案不存在!!")
        return {}

def __loadmemberfromjson():
    '''將資料由檔案取出放進dict'''
    filename = input("Enter filename to open? ")

    try:
        with open(filename, "rb") as f:
            return json.load(f)
    except TypeError:
        print(r"讀檔失敗!!")
        return {}
    except FileNotFoundError:
        print(r"檔案不存在!!")
        return {}


def savemembertopickle(team):
    '''將dict的資料放進檔案內'''
    filename = input(r"Enter filename to save? ")
    
    with open(filename, "wb") as f:
        pickle.dump(team, f)

    team={}


def savemembertojson(team):
    '''將dict的資料放進檔案內'''
    filename = input(r"Enter filename to save? ")
    json.dump(team, open(filename,"w"))
    team={}

def addmember(team):
    '''將資料放進dict'''
    id = input("New Employee Id? ")
    name = input("New Employee Name? ")

    result=__membersearch(team=team,tgid=id)

    if "-" in result:
        result=id+"已存在"
        print(result)
    else:
        team[id]=name
        result=id,"-",name,"新增完成"
        print(result)

def deletemember(team):
    '''刪掉dict內的資料'''
    tgid = input("Enter the id of member? ")
    result=__membersearch(team=team,tgid=tgid)
    if "-" in result:
        del team[tgid]
        result= tgid+"已刪除"
        print(result)
    else:
        result=tgid+"不是member"
        print(result)

def searchmember(team):
    '''找出dict內符合的資料'''
    item=input("input id or name?")
    if item=="id":
        tgid=input("input id:")
        result=__membersearch(team=team,tgid=tgid)
    else:
        tgname=input("input name:")
        result=__membersearch(team=team,tgname=tgname)
    
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
                #team=__loadmemberfrompickle()
                team=__loadmemberfromjson()
                

            showmember(team)
        
        elif an==2:
            if team!={}:
                #savemembertopickle(team)
                savemembertojson(team)
            else:
                print("無資料可以存檔!")
                break

        elif an==3:
            if team=={}:
                #team=__loadmemberfrompickle()
                team=__loadmemberfromjson()
                
            addmember(team)
        
        elif an==4:
            if team=={}:
                #team=__loadmemberfrompickle()
                team=__loadmemberfromjson()
                
            
            deletemember(team)

        elif an==5:
            if team=={}:
                #team=__loadmemberfrompickle()
                team=__loadmemberfromjson()
                
            searchmember(team)
        
        else:
            takeaway()
            
if __name__=="__main__":
    main()