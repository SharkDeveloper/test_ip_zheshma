from typing import List

from litestar import Controller, get, post, put, delete
from litestar.dto import DTOConfig
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, UserCreate, UserUpdate, UserResponse


class UserController(Controller):
    path = "/users"

    @get(
        description="Retrieve all users",
        summary="List Users",
        response_description="List of all users in the system"
    )
    async def get_users(self, db_session: AsyncSession) -> List[UserResponse]:
        query = select(User)
        result = await db_session.execute(query)
        users = result.scalars().all()
        return [UserResponse.model_validate(user) for user in users]

    @get(
        "/{user_id:int}",
        description="Retrieve a specific user by ID",
        summary="Get User",
        response_description="User details"
    )
    async def get_user(self, user_id: int, db_session: AsyncSession) -> UserResponse:
        query = select(User).where(User.id == user_id)
        result = await db_session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        return UserResponse.model_validate(user)

    @post(
        description="Create a new user",
        summary="Create User",
        response_description="Created user details"
    )
    async def create_user(
        self, data: UserCreate, db_session: AsyncSession
    ) -> UserResponse:
        user = User(**data.model_dump())
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        return UserResponse.model_validate(user)

    @put(
        "/{user_id:int}",
        description="Update an existing user",
        summary="Update User",
        response_description="Updated user details"
    )
    async def update_user(
        self,
        user_id: int,
        data: UserUpdate,
        db_session: AsyncSession,
    ) -> UserResponse:
        query = select(User).where(User.id == user_id)
        result = await db_session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        
        await db_session.commit()
        await db_session.refresh(user)
        return UserResponse.model_validate(user)

    @delete(
        "/{user_id:int}",
        description="Delete a user by ID",
        summary="Delete User",
        response_description="User successfully deleted"
    )
    async def delete_user(self, user_id: int, db_session: AsyncSession) -> None:
        query = select(User).where(User.id == user_id)
        result = await db_session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        await db_session.delete(user)
        await db_session.commit() 