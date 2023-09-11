"""Create user model

Revision ID: 81b34922d7f3
Revises: 4ade84002b50
Create Date: 2023-09-11 04:17:47.581257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "81b34922d7f3"
down_revision: Union[str, None] = "4ade84002b50"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("language_code", sa.String(length=5), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "language_code")
    # ### end Alembic commands ###
