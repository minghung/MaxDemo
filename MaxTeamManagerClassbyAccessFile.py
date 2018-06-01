import pickle
import json

'''永久儲存資料'''
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

def loadmemberfrompickle():
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

def loadmemberfromjson():
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