"""fix mistakes for task model

Revision ID: 56e1d1222b83
Revises: d0d693bcb22d
Create Date: 2024-11-08 01:45:30.051833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e1d1222b83'
down_revision = 'd0d693bcb22d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('goal_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('task_task_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'goal', ['goal_id'], ['id'])
        batch_op.drop_column('task_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('task_task_id_fkey', 'goal', ['task_id'], ['id'])
        batch_op.drop_column('goal_id')

    # ### end Alembic commands ###
