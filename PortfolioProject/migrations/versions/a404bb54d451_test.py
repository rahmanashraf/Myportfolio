"""test

Revision ID: a404bb54d451
Revises: d24a1d4b1fcd
Create Date: 2021-12-18 18:56:53.360006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a404bb54d451'
down_revision = 'd24a1d4b1fcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_name', sa.String(length=100), nullable=True),
    sa.Column('contact_email', sa.String(length=100), nullable=True),
    sa.Column('contact_message', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    # ### end Alembic commands ###
