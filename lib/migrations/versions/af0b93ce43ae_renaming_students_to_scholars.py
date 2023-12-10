"""Renaming students to scholars

Revision ID: af0b93ce43ae
Revises: 791279dd0760
Create Date: 2023-12-10 12:36:40.856944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af0b93ce43ae'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
