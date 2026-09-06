"""add users account or email unique

Revision ID: 46ccf80e43db
Revises: dc1cdab9f5f7
Create Date: 2026-09-06 13:13:15.038703

"""

from collections.abc import Sequence
from typing import Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "46ccf80e43db"
down_revision: Union[str, Sequence[str], None] = "dc1cdab9f5f7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        "users_account_unique", "users", ["account"], unique=True, if_not_exists=True
    )

    op.create_index(
        "users_email_unique", "users", ["email"], unique=True, if_not_exists=True
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("users_account_unique", "users", if_exists=True)
    op.drop_index("users_email_unique", "users", if_exists=True)
