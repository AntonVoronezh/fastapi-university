"""add aaaaaaa table

Revision ID: db64315c0c15
Revises: 3da4ec84a4c2
Create Date: 2023-01-12 18:48:46.532864

"""
import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db64315c0c15'
down_revision = '3da4ec84a4c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор записи Студента'),
    sa.Column('first_name', sa.String(length=255), nullable=False, comment='Имя Студента'),
    sa.Column('second_name', sa.String(length=255), nullable=False, comment='Отчество Студента'),
    sa.Column('family', sa.String(length=255), nullable=False, comment='Фамилия Студента'),
    sa.Column('age', sa.Integer(), nullable=False, comment='Возраст Студента'),
    sa.PrimaryKeyConstraint('id'),
    comment='Студенты'
    )
    op.create_table('user',
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('student_info',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор записи Информация о студенте'),
    sa.Column('description', sa.String(), nullable=False, comment='описание'),
    sa.Column('address', sa.String(), nullable=False, comment='адрес'),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Информация о студенте'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_info')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('student')
    # ### end Alembic commands ###