"""empty message

Revision ID: a7efcf378413
Revises: 48a798cb0848
Create Date: 2020-02-21 16:33:14.021716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7efcf378413'
down_revision = '48a798cb0848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('favorite_address_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customers', 'addresses', ['favorite_address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='foreignkey')
    op.drop_column('customers', 'favorite_address_id')
    # ### end Alembic commands ###
