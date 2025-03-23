"""empty message

Revision ID: 9c68289d675b
Revises: 5ba9d3909fa1
Create Date: 2025-03-24 01:07:15.902118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c68289d675b'
down_revision = '5ba9d3909fa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.drop_table('People')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('People',
    sa.Column('pid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('job', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
