from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    email: str = Field(max_length=50, nullable=False, unique=True)
    account: str = Field(max_length=50, nullable=False, unique=True)
    password: str = Field(max_length=255, nullable=False)
    verified_at: datetime | None = Field(alias="verified_at", nullable=True)
    created_at: datetime = Field(
        alias="created_at",
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
    )
    updated_at: datetime = Field(
        alias="updated_at",
        nullable=False,
        default_factory=lambda: datetime.now(timezone.utc),
    )
    deleted_at: datetime | None = Field(alias="deleted_at", nullable=True)
