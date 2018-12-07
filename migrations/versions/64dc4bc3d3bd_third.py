"""third

Revision ID: 64dc4bc3d3bd
Revises: 7339ed362038
Create Date: 2018-12-04 16:26:28.586481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64dc4bc3d3bd'
down_revision = '7339ed362038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('observations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timest', sa.String(length=50), nullable=True),
    sa.Column('date_of_observation', sa.String(length=20), nullable=True),
    sa.Column('oneviewid', sa.String(length=8), nullable=True),
    sa.Column('shift', sa.String(length=20), nullable=True),
    sa.Column('department', sa.String(length=50), nullable=True),
    sa.Column('area', sa.String(length=50), nullable=True),
    sa.Column('employee_exam', sa.String(length=20), nullable=True),
    sa.Column('activity', sa.String(length=20), nullable=True),
    sa.Column('attention_work', sa.String(length=20), nullable=True),
    sa.Column('attention_road', sa.String(length=20), nullable=True),
    sa.Column('appropriate_tools', sa.String(length=20), nullable=True),
    sa.Column('tools_is_ok', sa.String(length=20), nullable=True),
    sa.Column('ppe', sa.String(length=20), nullable=True),
    sa.Column('ppe_special', sa.String(length=20), nullable=True),
    sa.Column('capture', sa.String(length=20), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['oneviewid'], ['users.oneid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_observations_oneviewid'), 'observations', ['oneviewid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_observations_oneviewid'), table_name='observations')
    op.drop_table('observations')
    # ### end Alembic commands ###
