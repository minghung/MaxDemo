import sys
import MaxTeamManagerClassbyAccessFile as AccessFile

'''處理選單指令'''

def menu():
    menu=[
            {'itemDesc':'0.exit','func':takeaway},
            {'itemDesc':'1.show member','func':showmember},
            {'itemDesc':'2.save team member','func':AccessFile.savemembertojson},
            {'itemDesc':'3.add member','func':addmember},
            {'itemDesc':'4.delete member','func':deletemember},
            {'itemDesc':'5.search member','func':searchmember}
        ]

    while True:
        print ("input below number that you want to do:")
        for item in menu:
            print(item['itemDesc'])

        try:
            an=int(input("please enter a number of action(0~9):"))
            
            if an<1 or an >len(menu):
                raise ValueError
            break
        except:
            print(an," not a number,seclect again!!")
    return (an,menu[an]['func'])

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
        an, func=menu()
        if an==0:
            func()
        elif an==2:
            if team=={}:
                print("無資料可以存檔!")
            else:
                func(team)  
        else:
            if team=={}:
                if an==1:
                    print("將由檔案取出team member的清單!")
                team=AccessFile.loadmemberfromjson()
            func(team)
            
if __name__=="__main__":
    main()