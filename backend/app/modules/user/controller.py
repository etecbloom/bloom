from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.exc import IntegrityError

from .schema import CreateUserSchema, ResponseUserSchema, UserPartialUpdateSchema, UserLoginSchema
from .dependency import get_user_query_service, get_user_command_service

from app.modules.user.services.command_service import UserCommandService
from app.modules.user.services.query_service import UserQueryService

router = APIRouter(prefix="/users", tags=["users"])

# -------------------------------------------- CREATE ------------------------------------------------

@router.post(
    "", 
    response_model=ResponseUserSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_data: CreateUserSchema,
    service: Annotated[UserCommandService, Depends(get_user_command_service)]
) -> ResponseUserSchema:
    try:
        user = await service.create_user(user_data)
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

# ------------------------------------------ GET ---------------------------------------------

@router.get(
    "",
    response_model=List[ResponseUserSchema]
)
async def list_all_users(
    service: Annotated[UserQueryService, Depends(get_user_query_service)],
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    return await service.list_all_users(skip, limit)

@router.get(
    "/by_username/{username}",
    response_model=ResponseUserSchema,
)
async def get_by_username(
    username: str,
    service: Annotated[UserQueryService, Depends(get_user_query_service)]
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
    service: Annotated[UserQueryService, Depends(get_user_query_service)]
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
    service: Annotated[UserQueryService, Depends(get_user_query_service)]
) -> ResponseUserSchema:
    try: 
        return await service.get_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) 

# ------------------------------- DELETE ------------------------------------------------------------------------------

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
    service: Annotated[UserCommandService, Depends(get_user_command_service)] 
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
    
# ------------------------------------------------ PATCH -------------------------------------------------------- 

@router.patch(
    "/update_by_id/{id}",
    response_model=ResponseUserSchema
)
async def patch_user(
    id: int,
    patch_data: UserPartialUpdateSchema,
    service: Annotated[UserCommandService, Depends(get_user_command_service)]
) -> ResponseUserSchema:
    try:
        user = await service.patch_user(id, patch_data)
        return ResponseUserSchema.model_validate(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    

# ------------------------------------- LOGIN ------------------------------------------------------------------------

@router.post(
    "/login",
    response_model=ResponseUserSchema,
    status_code=status.HTTP_200_OK
)
async def login(
    login_data: UserLoginSchema,
    service: Annotated[UserQueryService, Depends(get_user_query_service)]
) -> ResponseUserSchema:
    try:
        user = await service.authenticate_user(login_data)
        return ResponseUserSchema.model_validate(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )