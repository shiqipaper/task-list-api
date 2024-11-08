"""add goal model

Revision ID: 0cf4c19a0211
Revises: f915a25fdfbc
Create Date: 2024-11-07 22:40:12.918789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf4c19a0211'
down_revision = 'f915a25fdfbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###