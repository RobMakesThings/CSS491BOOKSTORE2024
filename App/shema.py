import sqlalchemy
import json
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapped_column
Base = declarative_base()
class Book(Base):
    __tablename__ = 'Books'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    Author = sqlalchemy.Column(sqlalchemy.String)
    Title = sqlalchemy.Column(sqlalchemy.String)
    Genre = mapped_column(sqlalchemy.String)
    Price = sqlalchemy.Column(sqlalchemy.String)
    Description = sqlalchemy.Column(sqlalchemy.String)
class User(Base):
    __tablename__ = 'Users'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    Name = sqlalchemy.Column(sqlalchemy.String)
    Address = sqlalchemy.Column(sqlalchemy.String)
    Email = sqlalchemy.Column(sqlalchemy.String)
    Password = sqlalchemy.Column(sqlalchemy.String)

class Review(Base):
    __tablename__ = 'Reviews'    
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    Title_Id = mapped_column(sqlalchemy.ForeignKey("Books.id"))
    User_Id = mapped_column(sqlalchemy.ForeignKey("Users.id"))
    Title = sqlalchemy.Column(sqlalchemy.String)
    Score = sqlalchemy.Column(sqlalchemy.String)
    Body = sqlalchemy.Column(sqlalchemy.String)
    
class Supplier(Base):
    __tablename__ = 'Suppliers'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    companyName = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    Phone = sqlalchemy.Column(sqlalchemy.String)
class Order(Base):
    __tablename__ = 'Orders'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    customer_id= sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    totalPrice = sqlalchemy.Column(sqlalchemy.Integer)
    orderStatus =sqlalchemy.Column(sqlalchemy.String)
    orderItem_id = mapped_column(sqlalchemy.ForeignKey("orderItems.orderItem_id"))

class orderItem(Base):
    __tablename__ = 'orderItems'
    orderItem_id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    order_id = mapped_column(sqlalchemy.ForeignKey("Orders.id"))
    book_id = mapped_column(sqlalchemy.ForeignKey("Books.id"))
