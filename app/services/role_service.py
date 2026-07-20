from sqlalchemy.orm import Session

from app.models.role import Role
from app.models.industry import Industry


def create_role(
    db: Session,
    name: str,
    industry_id: int,
):
    """
    Create a new role.

    Returns:
        Role | None
    """

    industry = (
        db.query(Industry)
        .filter(Industry.id == industry_id)
        .first()
    )

    if not industry:
        return None

    existing = (
        db.query(Role)
        .filter(
            Role.name == name,
            Role.industry_id == industry_id,
        )
        .first()
    )

    if existing:
        return None

    role = Role(
        name=name,
        industry_id=industry_id,
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role


def get_roles(
    db: Session,
):
    """
    Return all roles.
    """

    return (
        db.query(Role)
        .order_by(Role.name)
        .all()
    )


def get_role(
    db: Session,
    role_id: int,
):
    """
    Return a single role.
    """

    return (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )


def get_roles_by_industry(
    db: Session,
    industry_id: int,
):
    """
    Return roles belonging to an industry.
    """

    return (
        db.query(Role)
        .filter(Role.industry_id == industry_id)
        .order_by(Role.name)
        .all()
    )


def update_role(
    db: Session,
    role_id: int,
    name: str,
    industry_id: int,
):
    """
    Update a role.

    Returns:
        Role | None
    """

    role = (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )

    if not role:
        return None

    industry = (
        db.query(Industry)
        .filter(Industry.id == industry_id)
        .first()
    )

    if not industry:
        return None

    role.name = name
    role.industry_id = industry_id

    db.commit()
    db.refresh(role)

    return role


def delete_role(
    db: Session,
    role_id: int,
):
    """
    Delete a role.

    Returns:
        bool
    """

    role = (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )

    if not role:
        return False

    db.delete(role)
    db.commit()

    return True
