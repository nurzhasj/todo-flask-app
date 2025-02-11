"""Initial migration.

Revision ID: 321f617222e5
Revises: 
Create Date: 2024-05-23 16:08:05.239625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '321f617222e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))
        batch_op.drop_column('data_created')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_created', sa.DATETIME(), nullable=True))
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###
