from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps.db import get_db

from app.schemas.industry import (
    IndustryCreate,
    IndustryUpdate,
    IndustryResponse,
)

from app.services.industry_service import (
    create_industry,
    get_industries,
    get_industry,
    update_industry,
    delete_industry,
)


router = APIRouter(
    prefix="/industries",
    tags=["Industries"],
)


@router.post(
    "",
    response_model=IndustryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    industry: IndustryCreate,
    db: Session = Depends(get_db),
):
    created = create_industry(
        db=db,
        name=industry.name,
    )

    if not created:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Industry already exists",
        )

    return created


@router.get(
    "",
    response_model=list[IndustryResponse],
)
def list_industries(
    db: Session = Depends(get_db),
):
    return get_industries(db)


@router.get(
    "/{industry_id}",
    response_model=IndustryResponse,
)
def get(
    industry_id: int,
    db: Session = Depends(get_db),
):
    industry = get_industry(
        db=db,
        industry_id=industry_id,
    )

    if not industry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Industry not found",
        )

    return industry


@router.put(
    "/{industry_id}",
    response_model=IndustryResponse,
)
def update(
    industry_id: int,
    payload: IndustryUpdate,
    db: Session = Depends(get_db),
):
    updated = update_industry(
        db=db,
        industry_id=industry_id,
        name=payload.name,
    )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Industry not found",
        )

    return updated


@router.delete(
    "/{industry_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete(
    industry_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_industry(
        db=db,
        industry_id=industry_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Industry not found",
        )

    return None
