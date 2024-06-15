import sqlalchemy
import json
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapped_column
from shema import *
from random import randint
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://apiAccess:hello@some_mariadb/BookStoreDB?charset=utf8mb4"
from faker import Faker
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:hello@127.0.0.1:3306/BookStoreDB")
Base = declarative_base()


fake = Faker()
def addNewBook(entries):
    
    
    batch = []
    for x in range(entries):
        
        newbook= { 
            "Title" : f"{fake.sentence()}",
            "Author" : fake.name(),
            "Genre" :"Biography",
            "Price" : randint(25,150),
            "Description" :f"{fake.paragraph(nb_sentences=10)}"
            }
        batch.append(newbook)
        print(batch)
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.insert(Book),batch)
        conn.commit()

def addUsers(entries):
    with engine.connect() as conn:
        batch = []
    # sqlalchemy.insert(Book).values(Title=f"{Title}", Author=f"{Author}",Price=f'{Price}',Genre=f'{Genre}')
        for x in range(entries):
            newUser= { 
            "Name" : fake.name(),
            "Address" : fake.address(),
            "Email" :fake.email(),
            "Password" : fake.password(),
            }
            batch.append(newUser)
        print(batch)
    
        result = conn.execute(sqlalchemy.insert(User),batch)
        conn.commit()

def addOrder(entries):
    with engine.connect() as conn:
        batch = []
        customers = conn.execute(sqlalchemy.text(f"""select id from Users order by RAND() Limit {entries}"""))
        Books = conn.execute(sqlalchemy.text(f"""select id from Books order by RAND() Limit {entries}"""))
        customers = list(customers)
        Books = list(Books)
        
        
        print(Books)
        for x in range(entries):
        # get order by taking a random amount of titles, a random cusotmer, and a random date. 
            newOrder= { 
            "customer_id" : str(customers[x]).strip("(,)"),
            "date" :  str(fake.date_time_this_year()),
            "orderStatus":"processessing"
            }
        
            batch.append(newOrder)
        print(batch)

        result = conn.execute(sqlalchemy.insert(Order),batch)
        conn.commit()
        batch = []
        orders = conn.execute(sqlalchemy.text(f"""select id from Orders order by RAND(5) """))
        orders = list(orders)
        for x in range(len(orders)):
            newOrderItem= { 
            "book_id" :str(Books[x%entries]).strip("(,)"),
            "quantity":randint(1,5),
            "order_id": str(orders[x]).strip("(,)")
            }
            batch.append(newOrderItem)
        result = conn.execute(sqlalchemy.insert(orderItem),batch)
        conn.commit()
def addSupplier(entries):

# need to somehow correlate suppliers with books. can come later. 
    batch = []
    for x in range(entries):
        newUser= { 
            "companyName" : fake.company(),
            "email" :fake.email(),
            "Phone" : fake.phone_number(),
            }
        batch.append(newUser)
    print(batch)
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.insert(Supplier),batch)
        conn.commit()
# addNewBook(50)
# addUsers(25)
# # addSupplier(5)
addOrder(15)
# #todo: add review
# print()