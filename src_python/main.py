import asyncpg
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Replace with your own database connection URL
DATABASE_URL = "postgresql://admin:admin@localhost:5432/user"

# Function to create a connection pool
async def get_pool():
    pool = await asyncpg.create_pool(DATABASE_URL)
    return pool

# Pydantic model for creating a new user
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.post("/users/", response_model=dict)
async def create_user(user: UserCreate, pool: asyncpg.Pool = Depends(get_pool)):
    async with pool.acquire() as connection:
        query = "INSERT INTO users (name, email, password) VALUES ($1, $2, $3) RETURNING id"
        values = (user.name, user.email, user.password)
        try:
            user_id = await connection.fetchval(query, *values)
            return {"id": user_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to create user: {str(e)}")

@app.get("/users/", response_model=list)
async def get_all_users(pool: asyncpg.Pool = Depends(get_pool)):
    async with pool.acquire() as connection:
        query = "SELECT * FROM users"
        try:
            result = await connection.fetch(query)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch users: {str(e)}")
