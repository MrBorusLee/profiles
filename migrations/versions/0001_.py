"""empty message

Revision ID: 0001
Revises: 
Create Date: 2024-04-30 22:42:33.414798

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "profiles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("dob", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("profiles")
