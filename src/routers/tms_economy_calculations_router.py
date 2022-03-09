from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import ORJSONResponse

from services import Web3LockService, get_lock_service


def web3_lock_service():
    return get_lock_service()


router = APIRouter(prefix="/lock")


@router.get("/lock/{id}")
async def get_lock_id(
    _id: Optional[str],
    service: Web3LockService = Depends(web3_lock_service),
):
    result = await service.get_lock_by_id(_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Calculation not found")
    return ORJSONResponse(result)
