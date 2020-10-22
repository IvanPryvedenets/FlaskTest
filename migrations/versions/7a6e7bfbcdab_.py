"""empty message

Revision ID: 7a6e7bfbcdab
Revises: 97f040c5445d
Create Date: 2020-10-22 18:14:43.275464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a6e7bfbcdab'
down_revision = '97f040c5445d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('story_tag',
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['story_id'], ['story.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('story_tag')
    # ### end Alembic commands ###
