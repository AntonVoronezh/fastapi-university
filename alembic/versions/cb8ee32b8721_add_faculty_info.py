"""add faculty_info

Revision ID: cb8ee32b8721
Revises: 0b623c4c5c17
Create Date: 2022-12-07 19:06:25.630456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8ee32b8721'
down_revision = '0b623c4c5c17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty_info',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор записи Информация о факультета'),
    sa.Column('description', sa.String(), nullable=False, comment='описание'),
    sa.Column('img', sa.String(), nullable=False, comment='картинка'),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Информация о факультете'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('faculty_info')
    # ### end Alembic commands ###
