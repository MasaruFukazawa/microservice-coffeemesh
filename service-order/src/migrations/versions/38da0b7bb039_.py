"""empty message

Revision ID: 38da0b7bb039
Revises: fa44e8ea7d7b
Create Date: 2024-05-31 04:19:46.688261

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "38da0b7bb039"
down_revision: Union[str, None] = "fa44e8ea7d7b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
