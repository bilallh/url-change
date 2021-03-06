"""empty message

Revision ID: 0b1c9ea11aef
Revises: 4913cb3f5a05
Create Date: 2021-10-04 17:14:01.414396

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b1c9ea11aef'
down_revision = '4913cb3f5a05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lifetime_coupon_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'lifetime_coupon', ['lifetime_coupon_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'lifetime_coupon_id')
    # ### end Alembic commands ###
