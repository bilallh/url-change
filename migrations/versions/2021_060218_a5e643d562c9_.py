"""empty message

Revision ID: a5e643d562c9
Revises: fc2eb1d7e4fc
Create Date: 2021-06-02 18:50:39.611746

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5e643d562c9'
down_revision = 'fc2eb1d7e4fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'salt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('salt', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
