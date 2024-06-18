#this file is what interacts with the database. Functions in the API are defined here.

import sqlalchemy
import json
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapped_column
from shema import *
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://apiAccess:hello@some_mariadb/BookStoreDB?charset=utf8mb4"

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# not secure for auth, better pass needed probably 
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://API:hello@127.0.0.1:3306/BookStoreDB")

Base = declarative_base()

columnOrder = ["Genre","id","Title","Author","Price",]
# columnOrder = ["id","code","name","description","Price"]

    
#read 
def findBookByTitle(search):
    
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.select(sqlalchemy.text("*")).where(Book.Title.like(f'{search}')))
        
        for row in result:
            print("title:", row.Title)
def findBookByid(id):
     print(id)
     with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(f'select * from Books where Books.id = {id}.'))
        # result = list(result)
        # print(list(result))
        return [row._asdict() for row in result]
        for row in result:
            print("title:", row.Title)
        
def findBookByAuthorOrTitle(search):
     with engine.connect() as connection:
        # result = connection.execute(sqlalchemy.text(f"""select * from Books where Author like '%{search}%' or Title like '%{search}%' Order by Title"""))
        result1 = sqlalchemy.text(f"""select * from Books where Author like '%{search}%' or Title like '%{search}%' Order by Title""")
        
        result2 = sqlalchemy.select(sqlalchemy.text("*")).where((Book.Author.like(f'%{search}%') )|(Book.Title.like(f'%{search}%')))
        print(result2)
        result = connection.execute(result2)
        # return  list(result)fe
        json_result= []
        print()
        result = list(result)
        for row in range(len(result)):
            current = {}
            for i in range(len(result[row])-1):
                # print(i)
                current[f"{columnOrder[i]}"]=result[row][i]
                
            json_result.append(current)
        print("im reading")
        return json_result
def findAllBooks():
     with engine.connect() as connection:
        # result = connection.execute(sqlalchemy.text(f"""select * from Books where Author like '%{search}%' or Title like '%{search}%' Order by Title"""))
        result = connection.execute(sqlalchemy.text(f"""select * from Books """))
        # return  list(result)
        json_result= [row._asdict() for row in result]
        return json_result
        json_result= []
            


#create
def addNewBook(Title,Author="Null",Genre="Null",Price='420'):

    newBook= sqlalchemy.insert(Book).values(Title=f"{Title}", Author=f"{Author}",Price=f'{Price}')

    with engine.connect() as conn:
        result = conn.execute(newBook)
        conn.commit()

#UPDATE
def updateBook(id, newTitle,Author,Genre,Price):
    # FIND RECORD TO UPDATE, THEN MAKE REQUIRED CHANGES. 

    findBook= sqlalchemy.update(Book).where(Book.id==id).values(Title=f"{newTitle}", Author=f"{Author}",Genre=f"{Genre}",Price=Price)

    with engine.connect() as conn:
        result = conn.execute(findBook)
        conn.commit()
#delete
def deleteBook(id):
    
    

    with engine.connect() as conn:
        print("imDeletin!")
        # return "imDeletin"
        
        
        result = conn.execute(sqlalchemy.select(Book).where(Book.id==id))
        resultDelete = conn.execute(sqlalchemy.delete(Book).where(Book.id==id).returning(Book.id,Book.Title))
        json_result= [row._asdict() for row in result]
        return json_result
        conn.commit()

# users need auth. will need to add cookie req to backend, and cookies to front. <<< 2/20, using JWT and built in stuff from fastapi
def addUser(Name, Address,Email,Password):
    new= sqlalchemy.insert(User).values(Name=f"{Name}", Address=f"{Address}",Email=f'{Email}',Password=f'{Password}')

    with engine.connect() as conn:
        result = conn.execute(new)
        conn.commit()
    pass
#need to add auth to get all users stuff for sure
def getUsers():
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(f"""select Name, Address , Email,id from Users """))
        json_result= [row._asdict() for row in result]
        return json_result

def loginUser(username,password):
    with engine.connect() as connection:
        print(username,password, "from front")
        # username= "spearshayley@example.com"
        # password="7hJqx5U7(a"
        result = sqlalchemy.select(User).where(User.Email==f"{username}")       
        
        result = connection.execute(result)
        connection.commit()
    
        # result = connection.execute(sqlalchemy.text(f"""select name from Users where Users.email = {str(username)} and Users.password={str(password)};"""))
        json_result= [row._asdict() for row in result]
        print(json_result,"json")
        return json_result
    
    
def updateUser(id,Name, Address,Email):
    update= sqlalchemy.update(User).where(User.id==id).values(Name=f"{Name}", Address=f"{Address}",Email=f"{Email}")
    with engine.connect() as conn:
        result = conn.execute(update)
        conn.commit()
    pass
def updateUserPass(id,Password):
    findUser= sqlalchemy.update(User).where(User.id==id).values(Password=f"{Password}")
    with engine.connect() as conn:
        result = conn.execute(findUser)
        conn.commit()
    pass
def delUser(id):
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.delete(User).where(User.id==id))
        conn.commit()
        return "sucess"
# need to add support for multiple books in here. 
# needs to send each title to orderItems table. make cart object 
def addOrder(customer_id,book_id):
    new= sqlalchemy.insert(Order).values(customer_id=f"{customer_id}", book_id=f"{book_id}")

    with engine.connect() as conn:
        conn.execute(new)
        conn.commit()
    pass

def getOrders():
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(f"""select Orders.id ,Users.Name,Users.Address,  Orders.date , Orders.orderStatus
from Orders 
join Users on Users.id = Orders.customer_id 
ORDER  by Orders.id;""")) 
        
        json_result= [row._asdict() for row in result]
        return json_result
    pass
def getOrder(search):
        with engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(f"""select Orders.id ,orderItems.quantity , Books.Title, Books.Price, Users.Name ,Users.Address 
from Orders
join orderItems on
Orders.id = orderItems.order_id and orderItems.order_id={search}
JOIN Books on 
Books.id = orderItems.book_id
Join Users on 
Users.id = Orders.customer_id ;""")) 
        
            json_result= [row._asdict() for row in result]
            return json_result
    
def updateOrder(id,customer_id,book_id):
    pass
def delOrder():
    pass

def addSupplier():
    pass
def getSuppliers():
    pass

def updateSupplier():
    pass
def delSupplier():
    pass
#TODO? CONVERT TO SESSIONS?
        
# make returns meangingfuller maYBE. finish database relational mapping. 
        #made returns json objects that js frontend can work with. 
# findBookByTitle("h")
# Session = sessionmaker()
# Session.configure(bind=engine)
# Session = Session()


# findBookByTitle = Session.execute(sqlalchemy.text('select * from Books where title like "%m%"'))
# print(str(findBookByTitle))
# select DISTINCT  Orders.id  ,Users.Name,Users.Address,  Orders.date, Books.Title, Books.Price, orderItems.quantity  
# from Orders 
# join Users on Users.id = Orders.customer_id 
# JOIN  orderItems on Orders.id = orderItems.order_id 
# join Books on Books.id = orderItems.book_id
# ORDER  by Orders.id;
