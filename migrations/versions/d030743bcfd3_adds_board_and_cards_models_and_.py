"""Adds Board and Cards models and registers blueprints to app

Revision ID: d030743bcfd3
Revises: 
Create Date: 2022-01-03 11:56:48.900368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd030743bcfd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('owner', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=180), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    op.drop_table('board')
    # ### end Alembic commands ###
