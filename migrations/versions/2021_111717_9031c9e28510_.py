"""empty message

Revision ID: 9031c9e28510
Revises: e6e8e12f5a13
Create Date: 2021-11-17 17:43:21.425167

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9031c9e28510'
down_revision = 'e6e8e12f5a13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('metric2', sa.Column('nb_deleted_directory', sa.Float(), nullable=True))
    op.add_column('metric2', sa.Column('nb_deleted_subdomain', sa.Float(), nullable=True))
    op.add_column('metric2', sa.Column('nb_directory', sa.Float(), nullable=True))
    op.add_column('metric2', sa.Column('nb_subdomain', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('metric2', 'nb_subdomain')
    op.drop_column('metric2', 'nb_directory')
    op.drop_column('metric2', 'nb_deleted_subdomain')
    op.drop_column('metric2', 'nb_deleted_directory')
    # ### end Alembic commands ###
