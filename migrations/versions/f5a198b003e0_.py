"""empty message

Revision ID: f5a198b003e0
Revises: b5088ebe0288
Create Date: 2022-02-10 22:28:17.651920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5a198b003e0'
down_revision = 'b5088ebe0288'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pokemon_team', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'pokemon_team')
    # ### end Alembic commands ###
