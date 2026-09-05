"""create users table

Revision ID: dc1cdab9f5f7
Revises:
Create Date: 2026-09-05 04:17:03.821100

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import TIMESTAMP, Integer, String
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision: str = "dc1cdab9f5f7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", Integer, primary_key=True, autoincrement=True),
        sa.Column("email", String, comment="電子郵件"),
        sa.Column("account", String, comment="帳號"),
        sa.Column("password", String, comment="密碼"),
        sa.Column("verified_at", TIMESTAMP, nullable=True, comment="驗證時間"),
        sa.Column(
            "created_at", TIMESTAMP, comment="新增時間", server_default=func.now()
        ),
        sa.Column(
            "updated_at", TIMESTAMP, comment="更新時間", server_onupdate=func.now()
        ),
        sa.Column("deleted_at", TIMESTAMP, comment="刪除時間", nullable=True),
    )

    op.create_table_comment("users", "用戶資料")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users", if_exists=True)
