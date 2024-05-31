"""empty message

Revision ID: fa44e8ea7d7b
Revises: 9b37f9222b95
Create Date: 2024-05-31 04:18:48.591275

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fa44e8ea7d7b"
down_revision: Union[str, None] = "9b37f9222b95"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
