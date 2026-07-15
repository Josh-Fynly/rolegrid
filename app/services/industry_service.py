from sqlalchemy.orm import Session

from app.models.industry import Industry


def create_industry(
    db: Session,
    name: str,
):
    """
    Create a new industry.

    Returns:
        Industry | None
    """

    existing = (
        db.query(Industry)
        .filter(Industry.name == name)
        .first()
    )

    if existing:
        return None

    industry = Industry(name=name)

    db.add(industry)
    db.commit()
    db.refresh(industry)

    return industry


def get_industries(
    db: Session,
):
    """
    Return all industries.
    """

    return (
        db.query(Industry)
        .order_by(Industry.name)
        .all()
    )


def get_industry(
    db: Session,
    industry_id: int,
):
    """
    Return a single industry.
    """

    return (
        db.query(Industry)
        .filter(Industry.id == industry_id)
        .first()
    )


def update_industry(
    db: Session,
    industry_id: int,
    name: str,
):
    """
    Update an industry.

    Returns:
        Industry | None
    """

    industry = (
        db.query(Industry)
        .filter(Industry.id == industry_id)
        .first()
    )

    if not industry:
        return None

    industry.name = name

    db.commit()
    db.refresh(industry)

    return industry


def delete_industry(
    db: Session,
    industry_id: int,
):
    """
    Delete an industry.

    Returns:
        bool
    """

    industry = (
        db.query(Industry)
        .filter(Industry.id == industry_id)
        .first()
    )

    if not industry:
        return False

    db.delete(industry)
    db.commit()

    return True
