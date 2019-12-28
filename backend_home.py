import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
if "mydatabase" not in dblist:
    mydb = myclient["homerental"]


def connect():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]


def insert(client_Name_text,address_text,year_text,rent_text, deposit_text):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]
    mylist = dict(Client_Name=client_Name_text, Address=address_text, Year=year_text, Rent=rent_text, Deposit=deposit_text)
    mycol.insert_one(mylist)
    view()

def view():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]
    rows = []
    for x in mycol.find({},{"_id":0}):
        rows.append(x)
    return rows

def search(client_name="",address="",year="",rent="",deposit=""):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]
    rows = []
    if client_name:
        myquery = dict(Client_Name=client_name)
        mydoc = mycol.find(myquery,{"_id":0})
        for x in mydoc:
            rows.append(x)
    elif address:
        myquery = dict(Address=artist)
        mydoc = mycol.find(myquery,{"_id":0})
        for x in mydoc:
            rows.append(x)
    elif year:
        myquery = dict(Year=int(year))
        mydoc = mycol.find(myquery,{"_id":0})
        for x in mydoc:
            rows.append(x)
    elif rent:
        myquery = dict(Rent=rent)
        mydoc = mycol.find(myquery,{"_id":0})
        for x in mydoc:
            rows.append(x)
    else:
        myquery = dict(Deposit=deposit)
        mydoc = mycol.find(myquery,{"_id":0})
        for x in mydoc:
            rows.append(x)        
    return rows


def delete(id):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]
    mydoc = mycol.find()
    c=0
    for x in mydoc:
        if id==c:
            mycol.delete_one(x)
        c += 1


def update(id,client_name,address,year,rent,deposit):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["homerental"]
    mycol = mydb["data"]
    mydoc=mycol.find()
    d=0
    for x in mydoc:
        if id==d:
            myquery = x
            newvalues = dict(Client_Name=client_name, Address=address, Year=year, Rent=rent, Deposit=deposit)
            newvalues1 = { "$set": newvalues }
            mycol.update_one(myquery, newvalues1)
        d += 1


connect()