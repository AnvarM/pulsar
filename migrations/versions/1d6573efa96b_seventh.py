"""seventh

Revision ID: 1d6573efa96b
Revises: 6a150b47c562
Create Date: 2018-12-04 18:10:00.515800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d6573efa96b'
down_revision = '6a150b47c562'
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
    sa.Column('employee_exam', sa.String(length=50), nullable=True),
    sa.Column('activity', sa.String(length=50), nullable=True),
    sa.Column('attention_work', sa.String(length=20), nullable=True),
    sa.Column('attention_road', sa.String(length=20), nullable=True),
    sa.Column('appropriate_tools', sa.String(length=20), nullable=True),
    sa.Column('tools_is_ok', sa.String(length=20), nullable=True),
    sa.Column('ppe', sa.String(length=20), nullable=True),
    sa.Column('ppe_special', sa.String(length=20), nullable=True),
    sa.Column('capture', sa.String(length=20), nullable=True),
    sa.Column('comment', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_observations_oneviewid'), 'observations', ['oneviewid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_observations_oneviewid'), table_name='observations')
    op.drop_table('observations')
    # ### end Alembic commands ###
