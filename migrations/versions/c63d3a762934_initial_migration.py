"""Initial migration

Revision ID: c63d3a762934
Revises: 
Create Date: 2024-08-11 21:28:45.804766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c63d3a762934'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('price', sa.String(length=50), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('square_footage', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('property_features', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('review', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['house_id'], ['properties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('properties')
    op.drop_table('contacts')
    # ### end Alembic commands ###
