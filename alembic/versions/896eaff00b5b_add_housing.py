"""add housing

Revision ID: 896eaff00b5b
Revises: cb8ee32b8721
Create Date: 2022-12-07 19:10:27.456536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '896eaff00b5b'
down_revision = 'cb8ee32b8721'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('housing',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор записи корпуса'),
    sa.Column('name', sa.String(length=255), nullable=False, comment='Название корпуса'),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Корпуса'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('housing')
    # ### end Alembic commands ###
