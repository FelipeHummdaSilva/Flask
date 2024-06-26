"""empty message

Revision ID: 0db1f792cc4b
Revises: 89261476b92c
Create Date: 2024-04-09 11:02:43.545511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db1f792cc4b'
down_revision = '89261476b92c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respondido', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('respondido')

    # ### end Alembic commands ###
