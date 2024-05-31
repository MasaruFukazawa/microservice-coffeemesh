"""empty message

Revision ID: 9b37f9222b95
Revises: a75caded853e
Create Date: 2024-05-31 03:23:46.368648

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9b37f9222b95"
down_revision: Union[str, None] = "a75caded853e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
