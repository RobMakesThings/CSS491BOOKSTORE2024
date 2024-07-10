from fastapi import FastAPI, Depends, HTTPException, status, Header, Response
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from database import *
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
# from jose import JWTError, jwt
import jwt

from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
app = FastAPI()
  
#need to make middleware more secure here. 
origins = [
    "http://127.0.0.1",
    "http://localhost:5173/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# make this better, the secret key probably needs to be stored in a enviroment file or something. 
fake_users_db ={}

app = FastAPI()
SECRET_KEY = "e8a73951a242fed7700b34d51f1f9232966c84c8b3f40fc4a22ea0fedeb15cb2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30





class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    Email: str | None = None



    
class User(BaseModel):
    id :int
    Name: str
    Email: str | None = None
    Address:str| None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, Email: str):
    if Email in db:
        user_dict = db[Email]
        return UserInDB(**user_dict)

# grabs user from database, checks if password matches hash, fails if not. 
def authenticate_user(Email: str, password: str):
    # print(Email,password)
    
    user = loginUser(Email,password)
    if not user:
        return False
    if not verify_password(password, user[0]["Password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login_for_access_token(
    
    
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    
    user = authenticate_user(form_data.username,form_data.password)
    print(form_data.username,form_data.password)
    print(user,"back from ")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user[0]}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.Email}]

#Create

@app.get("/add/{Title}:{Author}:{Genre}:{Price}")
async def addBook(Title,Author,Genre,Price):
    print("im creating a new one captain!S")
    return {"data":f' {addNewBook(Title,Author,Genre,Price)}'}

#Reading can be un authorized. This will go to the fontend, and can be intrepreted to the frontend

@app.get("/search/{author}")#returns only specified books by author or title
async def getBookByAuthorOrTitle(author):
    return {"data":findBookByAuthorOrTitle(author)}

@app.get("/searchAll/")#return all books
async def getAllBooks(response:Response):
    response.headers["X-Access-Control-Allow-Origin"] = "True"
    return {"data":findAllBooks()}

@app.get("/search/book/{id}")#return all books
async def getBook(id):
    # response.headers["X-Access-Control-Allow-Origin"] = "True"
    return {"data":findBookByid(id)}


#update
@app.get("/update/{id}:{newTitle}:{Author}:{Genre}:{Price}")#updates a book by given ID
async def updateExistingBook(id,newTitle,Author,Genre,Price):
    print("im updating an existing one captain!")
    return {"data":f' {updateBook(id,newTitle,Author,Genre,Price)}'}



#delete
@app.get("/delete/{id}")#delete a book by given ID
async def deleteBookById(id):
    return {"Deleted:":f"{deleteBook(id)}"}

# app.mount("/static", StaticFiles(directory="static"), name="static")
#change to post>>> handled by auth. 
@app.get("/user/login/{username}:{password}")



@app.get("/users/search/all")
async def getAllUsers(response:Response):
    # response.headers["X-Access-Control-Allow-Origin"] = "True"
    return {"data":getUsers()}
@app.get("/users/add/{Name}:{Address}:{Email}:{Password}")
async def addUser(Name,Address,Email,Password ):
    return {"data":addUser(Name,Address,Email,pwd_context.hash(Password))}
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


@app.post("/addOrder/{customer_id}")
async def newOrderAdd(customer_id):
    return {"data":newOrder(customer_id)}

@app.get("/addOrderItem/{id},{book_id},{quantity},")
async def newOrderItemAdd(id,book_id,quantity):
    return {"data":updateOrder(id,book_id,quantity)}
