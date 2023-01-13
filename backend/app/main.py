from fastapi import FastAPI, Path, HTTPException, Query, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Union, Any
from fastapi.middleware.cors import CORSMiddleware
from .models import User, Shipments, Transport_data
from mongoengine import connect
from mongoengine.queryset.visitor import Q
from pydantic import BaseModel, ValidationError
from passlib.context import CryptContext
from datetime import timedelta, datetime,  date
from jose import jwt
import json
# from models import User, Shipments, Transport_data

app = FastAPI()
connect(db="SCM", host="localhost", port=27017)
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5501",
    "http://localhost:5501",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewUser(BaseModel):
    username: str
    password: str = Query(
        regex='(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
    )


class NewShipment(BaseModel):
    Invoice_no: int
    container_no: int
    shipment_description: str
    route_details: str
    goods_type: str
    device: str
    expected_delivery_date: date
    PO_number: str
    delivery_no: int
    NDC_no: int
    batch_id: int
    Serial_no_of_goods: int


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_pass):
    return pwd_context.verify(password, hashed_pass)


@app.post("/sign_up", status_code=201)
def sign_up(new_user: NewUser):
    existing_user = json.loads(User.objects.filter(
        Q(username__icontains=new_user.username)).to_json())

    if len(existing_user) == 0:
        user = User(username=new_user.username,
                    password=get_password_hash(new_user.password))

        user.save()
        return{"message": "created new user"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="User with this email already exist"        
    )
    


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(username, password):
    try:
        user = json.loads(User.objects.get(username=username).to_json())
        return verify_password(password, user['password'])
    except User.DoesNotExist:
        return False


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "2fcb3d895799b8d8fe953b184d3c757d21c60514db6c62455f816939a2ff8703"
JWT_REFRESH_SECRET_KEY = "2fcb3d895799b8d8fe953b184d3c757d21c60514db6c62455f816939a2ff8703"


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    existing_user = json.loads(User.objects.filter(
        Q(username__icontains=form_data.username)).to_json())[0]

    if existing_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = existing_user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(existing_user['username']),
        "refresh_token": create_refresh_token(existing_user['username']),
    }


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


# @app.get("/user")
# def get_current_user(token: str = Depends(reuseable_oauth)):
#     try:
#         payload = jwt.decode(
#             token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
#         )

#         token_data = TokenPayload(**payload)

#         if datetime.fromtimestamp(payload['exp']) < datetime.now():
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Token expired",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#     except(jwt.JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     user: Union[dict[str, Any], None] = User.objects.filter(
#         Q(username=token_data.sub))[0].to_json()

#     return user


# print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh', get_current_user(
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzI0NzQwMTUsInN1YiI6Ik1hbm8ifQ.7EefwFkkcQgppuWhg94zEK6ha02XOVYtw4SVZVMRmtE"))

@app.post("/add_shipment", status_code=201)
def add_shipment(shipment: NewShipment, token: str = Depends(oauth2_scheme)):


    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(payload['exp']) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    new_shipment = Shipments(Invoice_no=shipment.Invoice_no,
                             container_no=shipment.container_no,
                             shipment_description=shipment.shipment_description,
                             route_details=shipment.route_details,
                             goods_type=shipment.goods_type,
                             device=shipment.device,
                             expected_delivery_date=shipment.expected_delivery_date,
                             PO_number=shipment.PO_number,
                             delivery_no=shipment.delivery_no,
                             NDC_no=shipment.NDC_no,
                             batch_id=shipment.batch_id,
                             Serial_no_of_goods=shipment.Serial_no_of_goods
                             )
    new_shipment.save()
    return {"message": "shipments created"}

@app.get("/deviceData")
def get_device_data(token: str = Depends(reuseable_oauth)):
    shipment_list = []
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(payload['exp']) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )      
    TransportData = Transport_data.objects().to_json()
    TransportData_list = json.loads(TransportData)
    return(TransportData_list)

@app.get("/checkValidity")
def validityCheck(token: str = Depends(reuseable_oauth)):
    shipment_list = []
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(payload['exp']) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True  
    



        
    
    