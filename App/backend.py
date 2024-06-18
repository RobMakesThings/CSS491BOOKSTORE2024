
#this file defines the endpoints for the API. CRUD operations, logins, etc. At the moment most of everything is a get request, but i plan on changing that. 
#based on examples from the FASTAPI website

from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from database import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
app = FastAPI()

#need to make middleware more secure here. 
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_users_db ={}

app = FastAPI()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    id :int
    Name: str
    Email: str | None = None
    Password:str | None = None
    Address:str| None = None
    

class UserInDB(User):
    Name: str


def get_user(db, username: str):
    print(db)
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

#not used 
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(form_data.username,form_data.password,"received")
    user_dict = loginUser(form_data.username,"$2b$12$Rmr5/be/IQf4sofCTvDUJOHYGnSgVz0mqd20.PiapEpU62PSuklrK")
    
    print(user_dict,"front")
    fake_users_db= user_dict[0]
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = user_dict 
    

    return {"access_token": user[0]["Name"], "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/")
async def root():
    return {"message": "world"}
#Create

@app.get("/add/{Title}:{Author}:{Genre}:{Price}")
async def addBook(Title,Author,Genre,Price):
    print("im creating a new one captain!S")
    return {"data":f' {addNewBook(Title,Author,Genre,Price)}'}

#Reading can be un authorized. This will go to the fontend, and can be intrepreted to the frontend

@app.get("/search/{author}")#returns only specified books by author or title
async def getBookByAuthorOrTitle(author):
    return {"data":findBookByAuthorOrTitle(author)}
@app.get("/search/book/{id}")
async def getBookByid(id):
    return {"data":findBookByid(id)}
@app.get("/searchAll/")#return all books
async def getAllBooks():
    return {"data":findAllBooks()}




#update-- should add 
@app.get("/update/{id}:{newTitle}:{Author}:{Genre}:{Price}")#updates a book by given ID
async def updateExistingBook(id,newTitle,Author,Genre,Price):
    print("im updating an existing one")
    return {"data":f' {updateBook(id,newTitle,Author,Genre,Price)}'}



#delete
@app.get("/delete/{id}")#delete a book by given ID
async def deleteBookById(id):
    return {"Deleted:":f"{deleteBook(id)}"}

app.mount("/static", StaticFiles(directory="static"), name="static")
#change to post
@app.get("/user/login/{username}:{password}")

async def login1(username,password):
    return {"data":loginUser(username,password)}



@app.get("/users/search/all")
async def getAllUsers():
    return {"data":getUsers()}
    
@app.get("/users/add/{Name}:{Address}:{Email}:{Password}")
async def addUser(Name,Address,Email,Password):
    return {"data":addUser(Name,Address,Email,Password)}
    
@app.get("/users/update/{id}:{Name}:{Address}:{Email}")
async def updateUser(id,Name,Address,Email):
    return {"data":updateUser(id,Name,Address,Email)}
    
#should be accepting a pass hash here if im being honest .. probably want the frontend to hash it? 
async def updateUserPass(id,Password):
    return {"data":updateUser(id,Password)}
    
@app.get("/user/delete/{id}")
async def delUser(id):
    return {"data":delUser(id)}
    

@app.get("/suppliers/search/all")
async def getAllSuppliers():
    return {"data":getSuppliers()}

@app.get("/orders/search/all")
async def getAllOrders():
    return {"data":getOrders()}
@app.get("/order/{id}")
async def getOrderItems(id):
    return {"data":getOrder(id)}
