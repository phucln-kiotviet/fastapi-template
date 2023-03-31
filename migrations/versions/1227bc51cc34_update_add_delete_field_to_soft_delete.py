"""update add delete field to soft delete

Revision ID: 1227bc51cc34
Revises: c6d07d91b19f
Create Date: 2023-03-31 13:48:06.629564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1227bc51cc34'
down_revision = 'c6d07d91b19f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('deleted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'deleted')
    # ### end Alembic commands ###