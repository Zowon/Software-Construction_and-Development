from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
from models import User
from starlette.responses import RedirectResponse

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the static files (including styles.css) from the "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# app = FastAPI()
templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create Database
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Root Route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

# 1. Signup
@app.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def signup(
    request: Request,  # Ensure request comes first
    db: AsyncSession = Depends(get_db),  # db dependency comes second
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    # Check if username or email already exists in the database
    query = select(User).filter((User.username == username) | (User.email == email))
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or Email already exists.")
    
    hashed_password = hash_password(password)
    new_user = User(username=username, email=email, hashed_password=hashed_password)
    
    try:
        db.add(new_user)
        await db.commit()
        return templates.TemplateResponse("success.html", {"request": request, "message": "Signup Successful!"})
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="An error occurred while creating the account.")

# 2. Login
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,  # Request comes first
    db: AsyncSession = Depends(get_db),  # db dependency second
    email: str = Form(...),
    password: str = Form(...),
):
    # Query the user by email
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    # If user is not found or password is incorrect, raise HTTPException
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password.")
    
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password.")
    
    return templates.TemplateResponse("welcome.html", {"request": request, "username": user.username})

# 3. Forgot Password
@app.get("/forgot-password", response_class=HTMLResponse)
async def forgot_password_form(request: Request):
    return templates.TemplateResponse("reset_password.html", {"request": request})

@app.post("/reset-password")
async def reset_password(
    request: Request,  # Request comes first
    db: AsyncSession = Depends(get_db),  # db dependency second
    email: str = Form(...),
):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=400, detail="Email not registered.")
    
    # Simulate sending an email (can be integrated with an actual email service)
    return templates.TemplateResponse("success.html", {"request": request, "message": "Reset link sent to your email!"})

# 4. Delete Account
@app.get("/delete-account", response_class=HTMLResponse)
async def delete_account_form(request: Request):
    return templates.TemplateResponse("delete_account.html", {"request": request})

@app.post("/delete-account")
async def delete_account(
    request: Request,  # Request comes first
    db: AsyncSession = Depends(get_db),  # db dependency second
    email: str = Form(...),
    password: str = Form(...),
):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    
    try:
        await db.delete(user)
        await db.commit()
        return templates.TemplateResponse("success.html", {"request": request, "message": "Account Deleted!"})
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="An error occurred while deleting the account.")

# 5. Logout
@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    # Clear user session or handle logout logic
    return RedirectResponse(url="/login")

