from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from .schema import CreateUserSchema, ResponseUserSchema
from .repository import UserRepository
from .service import UserService 
from .dependency import get_user_repository, get_user_service

from app.core.db.injection import get_db_session

router = APIRouter(prefix="/users", tags=["users"])

""" 
USER POST METHODS
"""

@router.post(
    "", 
    response_model=ResponseUserSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_data: CreateUserSchema,
    service: Annotated[UserService, Depends(get_user_service)]
) -> ResponseUserSchema:
    try:
        user = await  service.create_user(user_data)
        return ResponseUserSchema.model_validate(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=(str(e)))
    except IntegrityError as e:
        if "unique_constraint" in str(e).lower():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

""" 
USER GET METHODS
"""

@router.get(
    "/by_username/{username}",
    response_model=ResponseUserSchema,
)
async def get_by_username(
    username: str,
    service: Annotated[UserService, Depends(get_user_service)]
) -> ResponseUserSchema:
    try: 
        return await service.get_by_username(username)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get(
    "/by_email/{email}",
    response_model=ResponseUserSchema,
)
async def get_by_email(
    email: str,
    service: Annotated[UserService, Depends(get_user_service)]
) -> ResponseUserSchema:
    try: 
        return await service.get_by_email(email)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get(
    "/by_id/{id}",
    response_model=ResponseUserSchema,
)
async def get_by_id(
    id: int,
    service: Annotated[UserService, Depends(get_user_service)]
) -> ResponseUserSchema:
    try: 
        return await service.get_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) 


"""
USER DELETE METHODS
""" 

@router.delete(
    "/delete_by_id/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "User deleted successfully"},
        404: {"description": "User not found"},
        403: {"description": "Not enough permissions"}
    }
)
async def delete_by_id(
    id: int, 
    service: Annotated[UserService, Depends(get_user_service)] 
) -> None:
    try:
        deleted = await service.delete_by_id(id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {id} not found"
            )
        return None
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the user"
        )

    